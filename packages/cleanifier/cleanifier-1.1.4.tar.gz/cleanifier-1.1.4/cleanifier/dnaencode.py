
import numpy as np
from numba import njit, uint8, int64, uint64, prange

from .mask import Mask


U64_MINUSONE = uint64(np.iinfo(np.uint64).max)


# encoding DNA ###############################

def _get_table_dna_to_2bits(default=4):
    b = np.full(256, default, dtype=np.uint8)
    b[97] = 0   # a
    b[65] = 0   # A
    b[99] = 1   # c
    b[67] = 1   # C
    b[103] = 2  # g
    b[71] = 2   # G
    b[116] = 3  # t
    b[84] = 3   # T
    b[117] = 3  # u
    b[85] = 3   # U
    return b


_TABLE_DNA_TO_2BITS = _get_table_dna_to_2bits()


@njit(nogil=True, locals=dict(i=int64))
def _dna_to_2bits(x, table):
    for i in range(x.size):
        x[i] = table[x[i]]


# this is the one to use!
@njit(nogil=True)
def quick_dna_to_2bits(x):
    for i in range(len(x)):
        x[i] = _TABLE_DNA_TO_2BITS[x[i]]


@njit(nogil=True, parallel=True)
def parallel_dna_to_2bits(x):
    for i in prange(x.size):
        x[i] = _TABLE_DNA_TO_2BITS[x[i]]


# numba compile error
# @njit(nogil=True, locals=dict(seq=uint8[:], table=uint8[:]))
def dna_to_2bits(seq, table=_TABLE_DNA_TO_2BITS):
    # we expect seq to be a bytearray
    # xx = np.array(seq, dtype=np.uint8)
    if isinstance(seq, bytes):
        xx = np.frombuffer(bytearray(seq), dtype=np.uint8)
    else:
        xx = np.frombuffer(seq, dtype=np.uint8)
    _dna_to_2bits(xx, table)
    return xx


_TABLE_BITS_TO_DNASTR = ["A", "C", "G", "T"]


def qcode_to_dnastr(qcode, q, table=_TABLE_BITS_TO_DNASTR):
    qc = int(qcode)
    return "".join([table[((qc >> (2 * (q - i - 1))) & 3)] for i in range(q)])


@njit(nogil=True, locals=dict(base=uint64))
def write_qcode_to_buffer(qcode, q, buf, start):
    for i in range(q):
        base = (qcode >> (2 * (q - i - 1))) & 3
        buf[start + i] = uint8(base)


# no need to njit!
def _get_table_2bits_to_dna(default=4):
    b = np.full(256, 35, dtype=np.uint8)  # fill with b'#'
    b[0] = 65
    b[1] = 67
    b[2] = 71
    b[3] = 84
    b[default] = 78
    return b


_TABLE_2BITS_TO_DNA = _get_table_2bits_to_dna()


@njit(nogil=True)
def twobits_to_dna_inplace(buf, start=0, end=0):
    if end <= 0:
        end = len(buf) - end
    for i in range(start, end):
        buf[i] = _TABLE_2BITS_TO_DNA[buf[i]]


# ########## reverse complements and canonical representation ##############

@njit(nogil=True,
    locals=dict(c1=uint8, c2=uint8, n=int64, drei=uint8))
def revcomp_inplace(seq):
    n = seq.size
    drei = 3
    for i in range((n + 1) // 2):
        j = n - 1 - i
        c1 = seq[i]
        c2 = seq[j]
        seq[j] = drei - c1 if c1 < 4 else c1
        seq[i] = drei - c2 if c2 < 4 else c2


@njit(nogil=True, locals=dict(
    c=uint8, n=int64, drei=uint8, rc=uint8[:]))
def revcomp_to_buffer(seq, rc):
    n = seq.size
    drei = 3
    for i in range(n):
        c = seq[n - 1 - i]
        rc[i] = drei - c if c < 4 else c


@njit(nogil=True, locals=dict(rc=uint8[:]))
def revcomp(seq):
    rc = np.empty_like(seq, dtype=np.uint8)
    revcomp_to_buffer(seq, rc)
    return rc


@njit(nogil=True, locals=dict(
    code=uint64, drei=uint64, rc=uint64, c=uint64))
def revcomp_code(code, q):
    # only works for 0 <= q <= 31 !
    # when using uints, due to a potential bug in numpy/numba,
    # we would have to re-declare code as uint64 locally.
    drei = uint64(3)
    rc = 0
    for i in range(q):
        c = drei - (code & drei)
        rc = (rc << 2) | c
        code >>= 2
    return rc


@njit(nogil=True, locals=dict(
    code=uint64, c=uint64))
def _get_rctable():
    rctable = np.zeros(256, dtype=np.uint64)
    for c in range(256):
        rctable[c] = revcomp_code(c, 4)
    return rctable


_RCTABLE = _get_rctable()


@njit(nogil=True, locals=dict(
    code=uint64, rc=uint64, c=uint64))
def revcomp_code_table(code, q):
    rc = 0
    while q >= 4:
        c = _RCTABLE[code & 255]
        rc = (rc << 8) | c
        code >>= 8
        q -= 4
    for i in range(q):
        c = 3 - (code & 3)
        rc = (rc << 2) | c
        code >>= 2
    return rc


@njit(nogil=True, locals=dict(
    code=int64, rc=int64))
def canonical_code(code, q):
    rc = revcomp_code(code, q)
    return code if code <= rc else rc


def compile_revcomp_and_canonical_code(q, rcmode):
    """
    return pair of functions (revcomp_code_q, canonical_code_q)
    specialized for q-gram codes for the given value of q.
    It is expected that LLVM optimization does loop unrolling.
    """
    @njit(nogil=True, locals=dict(
        code=uint64, rc=uint64, c=uint64))
    def _rc(code):
        rc = 0
        t = q // 4
        for i in range(t):
            c = _RCTABLE[code & 255]
            rc = (rc << 8) | c
            code >>= 8
        r = q % 4
        for i in range(r):
            c = 3 - (code & 3)
            rc = (rc << 2) | c
            code >>= 2
        return rc
    
    if rcmode == "min":
        @njit(nogil=True, locals=dict(
            code=uint64, rc=uint64))
        def _cc(code):
            rc = _rc(code)
            return code if code <= rc else rc
    elif rcmode == "max":
        @njit(nogil=True, locals=dict(
            code=uint64, rc=uint64))
        def _cc(code):
            rc = _rc(code)
            return code if code >= rc else rc
    elif rcmode == "r":
        @njit(nogil=True, locals=dict(
            code=uint64, rc=uint64))
        def _cc(code):
            rc = _rc(code)
            return rc
    else:  # 'f', 'both', ...
        @njit(nogil=True, locals=dict(
            code=uint64, rc=uint64))
        def _cc(code):
            return code

    return _rc, _cc


# translation of a DNA buffer into codes
def compile_twobit_to_codes(tmask, rcmode, invalid=U64_MINUSONE):
    # tmask should be a mask tuple, but might be an int in some cases
    if isinstance(tmask, int):
        k = w = tmask  # be safe here
        tmask = tuple(range(k))
    elif isinstance(tmask, Mask):
        k = tmask.k
        w = tmask.w
        tmask = tmask.tuple
    elif type(tmask) is tuple:
        k, w = len(tmask), tmask[-1] + 1
    else:
        raise ValueError(f"mask type {type(tmask)} is not supported.")
    _, ccc = compile_revcomp_and_canonical_code(k, rcmode)

    @njit(nogil=True, locals=dict(code=uint64))
    def twobit_to_codes(seq, out, start=0, n=-1):
        """write n (or all) canonical k-mer codes from seq[start...] into out buffer"""
        if n == -1:
            n = len(seq) - w + 1 - start
        for i in range(start, start + n):
            code = 0
            for j in tmask:
                c = seq[i + j]
                if c >= 4:
                    out[i - start] = uint64(invalid)
                    break
                code = (code << 2) | c
            else:
                code = ccc(code)
                out[i - start] = code

    @njit(nogil=True, locals=dict(code=uint64))
    def twobit_to_code(seq, start=0):
        """return a single canonical code at seq[start...]"""
        code = 0
        for j in tmask:
            c = seq[start + j]
            if c >= 4:
                return uint64(invalid)
            code = (code << 2) | c
        else:
            code = ccc(code)
            return code

    return twobit_to_codes, twobit_to_code
