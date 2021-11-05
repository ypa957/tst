import random
import time
import numpy as np

a = []
for i in range(1000000):
    a.append(random.random())


t1 = time.time()
sum1 = sum(a)
t2 = time.time()

b = np.array(a)
t4 = time.time()
sum3 = np.sum(b)
t5 = time.time()

print(t2-t1, "-----------", t5-t4)

print(t1)
print(t2)
