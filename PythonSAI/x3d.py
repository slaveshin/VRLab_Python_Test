import time
start = time.time()
from .concrete import *
end = time.time()
print("X3D package loading is complete")
print("The time used to execute this is given below : %0.4f ms" % ((end-start) * 1000))
