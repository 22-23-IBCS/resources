
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

def main():
    #print("Hello World")

    print("Hey welcome to the car creator look at this new car it is...")
    
    veh1 = Vehicle("Toyota", "blue")
    b = veh1.getBrand()
    print(b)
    veh1.setBrand("Bugatti")
    print(veh1.getBrand())
    

if __name__ == "__main__":
    main()
