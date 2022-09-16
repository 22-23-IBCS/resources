class CarnivorousPlant:

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

class Nepenthes(CarnivorousPlant):

    def __init__(self, b, col):
        self.name = "Rajah"
        super().__init__(b, col)

    def getName(self):
        return self.name

def main():
    #print("Hello World")

    print("Hey welcome to the plant picker look at this new carnivorous plant...")
    
    p1 = CarnivorousPlant("Fly Trap", "green")
    print(p1.getBrand())
    p2 = Nepenthes("Nepenthes", "red")
    print(p2.getName())
    print(p2.getBrand())
    

if __name__ == "__main__":
    main()
