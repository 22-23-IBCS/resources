
class Vehicle:

    #constructor method. Needed to define how
    #the class instances are created
    def __init__(self, b, col):
        self.numWheels = 4
        self.brand = b
        self.color = col

    def getBrand(self):
        return self.brand

    def setBrand(self, b):
        self.brand = b

class Truck(Vehicle):

    def __init__(self):
        self.load = 5
        super().__init__("Ford", "black")

    def unload(self):
        self.load = 0

    def addLoad(self):
        self.load += 1

    def getLoad(self):
        return self.load

def main():
    #print("Hello World")

    print("Hey welcome to the car creator look at this new car it is...")
    
    veh1 = Vehicle("Toyota", "blue")
    b = veh1.getBrand()
    print(b)
    T = Truck()
    print(T.getBrand())
    T.unload()
    for i in range(4):
        T.addLoad()
    print(T.getLoad())
    print(T.load)
    
    

if __name__ == "__main__":
    main()
