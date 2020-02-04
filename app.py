# def s(x, y):
#   return x + y

# print s(3, 9)

# def fibonacci(n):
#   a, b, c = 0, 1, 1
#   while c<n:
#     a, b, c = b, a+b, c+1
#     print(b)

# print fibonacci(45)

# # import time

# # start = time.time()

# # liste_1 = []
# # for i in range (10000000):
# #   liste_1.append(i**2)

# # end = time.time()

# # print(end-start)

# # start = time.time()

# # liste_2 = [i**2 for i in range (10000000)]

# # end = time.time()

# # print(end-start)





# import random



# print(random.choice(["jean", "anne", "julie"]))

# import glob

# print(glob.glob("*"))

import numpy as np

# A = np.array([1, 2, 3])

# print A.ndim
# print A.shape

# B = np.zeros((10, 10))

# print type(B.shape)

# C = np.ones((10, 10))

# print C

# print (np.random.rand(3, 4))

# D = np.zeros((3, 2))
# E = np.ones((3, 2))

# print np.concatenate((D, E), axis=1)

def initialisation(m, n):
  X = np.random.randn(m , n)
  X = np.concatenate((X, np.ones((X.shape[0], 1))), axis = 1)

  return X

print initialisation(12, 2)
