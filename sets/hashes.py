from functools import reduce

"""
Implementation of various hashes described in
http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx
"""

def of(item):
    yield hash(item)
    for fn in (rotating, bernstein, shiftaddxor, fnv, elf):
        yield reduce(fn, [ord(b) for b in item])

def rotating(state, byte):
    return (state << 4) ^ (state >> 28) ^ byte

def bernstein(state, byte):
    return 33 * (state ^ byte)

def shiftaddxor(state, byte):
    return state ^ ((state << 5) + (state >> 22) + byte)

def fnv(state, byte):
    if state == 0: state = 0x811c9dc5
    return (state * 0x1000193) ^ byte

def elf(state, byte):
    state = (state << 4) + byte
    g = state & 0xf0000000
    if g != 0: state ^= g >> 24
    state &= ~g
    return state
