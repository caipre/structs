import hashes

class BloomFilter(object):
    def __init__(self, m=256):
        self.m = m
        self.bits = [0 for i in range(m)] # this is horrible

    def put(self, item):
        for sum in hashes.of(item):
            self.bits[sum % self.m] = 1

    def __contains__(self, item):
        for sum in hashes.of(item):
            if not self.bits[sum % self.m]:
                return False
        return True # maybe True

bf = BloomFilter()
bf.put("hello")
bf.put("world")
assert "hello" in bf
assert "world" in bf
assert "nope" not in bf
