import Pyro4

alist,key = [1,3,3,4,3,5,7,7,7,7,7,7,9],7 # Example list and key

res = Pyro4.Proxy("PYRONAME:LoadBalancer")

res = res.roundRobin(alist,key)

print("################################")

print(alist," looking key: ",key)

print("Counter is: ",res[0])

print("This request served by server ", res[1])

print("################################")