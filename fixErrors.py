# IBCS "Find my error"

# Each method below currently does not run properly. Either it throws an error
# or it prints out/returns the wrong thing. Fix each method one by one.
# Comment out the method call in the main to run it and test it.


#calculate sum, product and mean of three numbers
def calcThree(x, y, z):
    x = x + y + z
    y = x*y*z
    z = (x+y+z)/3
    return x, y, z

#determine the minimum value in a list of numbers
def myMin(L):
    m = 0
    for e in L:
        if e < m:
            m = e

    return m

#determine the average number of characters in a word
def sentenceData():
    sen = input("Please type a sentence.\n")
    senWords = sen.split()
    numWords = len(senWords)
    totalChar = 0
    for w in range(numWords):
        totalChar = len(w)

    print("The average word length is: " + str(round(totalChar/numWords, 2)))

#randomize the characters in a user input name (First and Last)
# and print out the users new name
def randomName():
    name = input("Please enter your first name")
    name2 = input("Please enter your last name")
    for n in name:
        name = name + random.choice(name)
    for n in name2:
        name2 = name2 + random.choice(name2)

    print("Hello" + name + " " name2)


def main():
    #calcThree()
    #myMin()
    #sentenceData()
    #randomName()


if __name__ == "__main__":
    main()
