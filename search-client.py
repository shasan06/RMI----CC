import Pyro4

import random

alist,prev = [],0

# code to generate a list of random numbers in ascending order
for i in range(100):
    current = random.randint(1,10) + prev
    alist.append(current)
    prev = current

print(alist)

key = int(input("Give a key to search: "))

# use the name server object to lookup uri shortcut called search
res = Pyro4.Proxy("PYRONAME:search")

# I call the LinearSearch by passing the list and the key
print(res.LinearSearch(alist,key))
