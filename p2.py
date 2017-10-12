class Box(object):
    def __init__(self, ival):
        self.value = ival
    __cmp__(self, other)
        b0 = Box(0)
        b1 = Box(1)
        b2 = Box(2)
        b3 = Box(3)
        print(b2 < b2)
        print(b2 <= b2)
        print(b2 >= b1)
        print(b3 > b2)
        print(b0 != b0)
        print(b0 == b0)
