class Coffeeshop:

    def __init__(self):
        self.coffee = 3.5

    def calculatePrice(self, order):
        if order == "coffee":
            return self.coffee
        else:
            return "We don't have that here"
        

def main():

    C = Coffeeshop()
    print("Welcome to the shop!")
    #need to assign a variable name to the input
    myOrder = input("What do you want?\n")

    print("This costs " + str(C.calculatePrice(myOrder)))
    

if __name__ == "__main__":
    main()
