class Zoo:

    def __init__(self):
        #how to create the initial instance of a zoo
        self.name = "Point Defiance Zoo"
        self.animals = ["Elephant", "Penguin", "Python", "Orangutan", "Fish"]
        self.employees = ["Steve", "Harold", "Bart", "Dembele"]
        self.enclosures = {1 : "Savannah", 2 : "Ice", 3 : "Jungle", 4 : "Pond"}
        self.habitats = {"Elephant" : 1,
                         "Penguin" : 2,
                         "Python" : 3,
                         "Orangutan" : 3,
                         "Fish" : 4}

    def getName(self):
        return self.name

    def getAnimals(self):
        return self.animals

    def getEmployees(self):
        return self.employees

    #a method to change data for our class
    def updateAnimals(self, animal, habitat):
        self.animals.append(animal)

        for enclosure in self.enclosures.keys():
            if habitat == self.enclosures.get(enclosure):
                self.habitats.update({animal : enclosure})
                print(animal, enclosure)

    def getHabitat(self, animal):
        h = self.habitats.get(animal)
        name = self.enclosures.get(h)
        print("The " + animal + " lives in the " + name)
        

def main():

    #create a zoo
    Z = Zoo()
    print(Z.getName())
    Z.updateAnimals("Zebra", "Savannah")
    print(Z.getAnimals())

    Z.getHabitat("Penguin")
    Z.getHabitat("Orangutan")
    Z.getHabitat("Zebra")
    


if __name__ == "__main__":
    main()
