import time
import math

start = time.time()
math.factorial(1000000)
end = time.time()

print(f"{end - start:.5f}sec")
