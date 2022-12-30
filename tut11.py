# a = set()
# print(type(a))
l=[1, 2, 4, 4, 6, 8]
s_from_l=set(l)
print(l)
print(s_from_l)

s_from_l.add(67)
print(s_from_l)
s_from_l.add(3)
print(s_from_l)

s_from_l.remove(6)
print(s_from_l)