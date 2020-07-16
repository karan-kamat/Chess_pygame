# class ab:
#     a = 6
#     b = 3
#
#
# f = ab()
# print(f.a, f.b)
# g = f
# g.a = "This"
# g.b = "Sucks"
# print(f.a, f.b)


# class ab:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def copy(self):
#         return ab(self.a, self.b)
#
#     def sh(self):
#         print(self.a, self.b)
#
#
# f = ab(5, 3)
# g = f.copy()
# f.sh()
# g.sh()
# print(type(f), type(g))
# print(f == g)
# print(f is g)


# p = [(i, j) for i in range(8) for j in range(8)]
# print(p)

# def z(a):
#     return 2*a
#
#
# def y(b):
#     return b+5
#
#
# rez = z
# rey = y(z)
# print(rey(6))
# print(y(5))

# s="rdcfgvhbj"
# print(s.upper())
# print(str.upper(s))

# def g():
# 	i=0
# 	while i<5:
# 		yield i
# 		i+=1
# g=g()
# print(next(g()))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# import re
# print("qwert34yuio$pasd@fghjklzxcvbnm".split(r""))
# h
