# import Pyro4

# x, y = [1,2,3], [3,5,7]

# res = Pyro4.Proxy("PYRONAME:models")

# print(res.estimate_coef(x,y))

import Pyro4

import random

x, y = [1,2,3,4,5], [5,7,9,11,13]

res = Pyro4.Proxy("PYRONAME:models")

x,y = (res.estimate_coef(x,y))

print(str(x)+"*x + "+str(y))