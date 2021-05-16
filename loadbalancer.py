import Pyro4

@Pyro4.expose

class LoadBalancer(object):

    c=0 # a counter is set to zero, counter will be 0 for LB1 and 1 for LB2
    def callServer(self,name,alist,key): # A method to call servers
        res = Pyro4.Proxy(name) # pass the name of the server
        result = res.myCount(alist,key) # Pass the list and the key
        return result # return the results from server

    def roundRobin(self,alist,key): # implement the round robin
        print("Load balancer used: LB-"+ str(LoadBalancer.c))

        if LoadBalancer.c==0: # Access the class variable
            result = LoadBalancer.callServer(self,"PYRONAME:Server1",alist,key)
            LoadBalancer.c=1
            return result
        else:
            result = LoadBalancer.callServer(self,"PYRONAME:Server2",alist,key)
            LoadBalancer.c=0
            return result # return the results to the client

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(LoadBalancer)
ns.register("LoadBalancer", uri)
print("Load balancer is live!")
daemon.requestLoop()



