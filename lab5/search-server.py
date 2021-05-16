import Pyro4

@Pyro4.expose

class Search(object):
    def LinearSearch(self, alist, key):
        for i in alist:
            if i == key:
                return True
        return False

daemon = Pyro4.Daemon()

# find the name server

ns = Pyro4.locateNS()
uri = daemon.register(Search)

# register the object in the name server as search
ns.register("search", uri)
print("Ready.")
daemon.requestLoop()

