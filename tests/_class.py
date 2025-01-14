class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    
a = A(1, 2)
assert a.add() == 3
assert a.sub() == -1

assert a.__base__ is object

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def add(self):
        return self.a + self.b + self.c

    def sub(self):
        return self.a - self.b - self.c

assert B.__base__ is A    

b = B(1, 2, 3)
assert b.add() == 6
assert b.sub() == -4

class C(B):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def add(self):
        return self.a + self.b + self.c + self.d

    def sub(self):
        return self.a - self.b - self.c - self.d
    
assert C.__base__ is B

c = C(1, 2, 3, 4)
assert c.add() == 10
assert c.sub() == -8

class D(C):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d)
        self.e = e

    def add(self):
        return super().add() + self.e

    def sub(self):
        return super().sub() - self.e
    
assert D.__base__ is C

d = D(1, 2, 3, 4, 5)
assert d.add() == 15
assert d.sub() == -13

assert isinstance(1, int)
assert isinstance(1, object)
assert isinstance(C, type)
assert isinstance(C, object)
assert isinstance(d, object)
assert isinstance(d, C)
assert isinstance(d, B)
assert isinstance(d, A)
assert isinstance(object, object)
assert isinstance(type, object)