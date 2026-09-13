# 1. Define the blueprint template

class Router:
    def __init__(self, hostname, model):
        self.hostname = hostname     # Public attribute
        self.model = model           # Public attribute



# 2. Deploy Live instances (Objects) into memory
r1 = Router("Core-01", "Cisco-ISR")
r2 = Router("Edge-02", "Arista-7050")


#3. Read the state data out of the objects
print(r1.hostname)
print(r2.hostname)