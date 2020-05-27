class A:
    pass


class B:
    pass


class C:
    pass


class X(A, B):
    pass


class Y(B, C):
    pass


class Z(X, Y, C):
    pass


class M(Z, C, A):
    pass


print(M.__mro__)
