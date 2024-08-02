import copy
#shallow copy & deep copy
a = [1,2,3]
b = a
print(a, b)
print(id(a), id(b))
a[0] = 6
print(a, b)
print(id(a), id(b))

s = [1, 2, 3]
t = copy.deepcopy(s)
print(s, t)
print(id(s), id(t))
s[0]=6
print(s, t)
print(id(s), id(t))
