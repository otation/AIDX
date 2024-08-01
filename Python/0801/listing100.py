import random

a = []

for i in range(1, 11, 1):
 b = (random.randint(1,100))
 a.append(b)

a.sort()
print(a)

del(a[0])
del(a[-1])

print(a)

sum = 0
type(sum)

for j in a:
    sum += j

print("합계는 : " ,sum)
print("평균값은 :" ,sum/len(a))

import numpy

print(numpy.mean(a))