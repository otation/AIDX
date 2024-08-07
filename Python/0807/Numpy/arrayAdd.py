import numpy as np

A = np.array([1,2,3,4])
B = np.array([5,6,7,8])
twoDim = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(twoDim)
print(twoDim[0][0])
print(twoDim[0][1])
print(twoDim[0][2])

result = A + B
print(result)

result3 = A < 3
print(result3)