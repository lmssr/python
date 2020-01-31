def s(x, y):
  return x + y

print s(3, 9)

def fibonacci(n):
  a, b, c = 0, 1, 1
  while c<n:
    a, b, c = b, a+b, c+1
    print(b)

print fibonacci(45)

# import time

# start = time.time()

# liste_1 = []
# for i in range (10000000):
#   liste_1.append(i**2)

# end = time.time()

# print(end-start)

# start = time.time()

# liste_2 = [i**2 for i in range (10000000)]

# end = time.time()

# print(end-start)





import random



print(random.choice(["jean", "anne", "julie"]))

import glob

print(glob.glob("*"))













