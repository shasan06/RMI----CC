import Pyro4

import random

import time

x, y = [1,2,3,4,5], [5,7,9,11,13]

proxy = Pyro4.Proxy("PYRONAME:models")

proxy._pyroAsync()

asyncresult = proxy.estimate_coef(x,y)

print("value available?", asyncresult.ready)

time.sleep(5) # sleep for 5 seconds

print("resultvalue=", asyncresult.value)

print("value available?", asyncresult.ready)