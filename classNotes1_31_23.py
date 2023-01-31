import random

def CentralTendencies(x, y, z):
    #mean
    mean = (x + y + z)/3

    #median
    if x < y:
        if y < z:
            median = y
        else:
            if x < z:
                median = z
            else:
                median = x
    else:
        if x < z:
            median = x
        else:
            if y < z:
                median = z
            else:
                median = y

    return mean, median


def Khang():
    n = random.randint(1,10)
    if n < 5:
        print("Khang!")
    else:
        print("Harry...")

    return n, "Finn"
    

def Junha():
    for i in range(5):
        for char in "Junha":
            print(char)


def main():

    #data types (Strings, Integers, Floats)

    name = "Adwaya"
    name2 = "Joseph"
    #concatenation
    print(name + " " + name2)
    #indexing
    print(name[4])
    #substrings
    print(name2[0:2])
    print(name[1:])
    print(name2[:4])

    x = 10
    print(x)
    print(x + 5)
    print(x * 2)
    # mod operator
    print(x % 3)
    # integer division ("div")
    print(x // 3)
    #can change data type
    y = x/3
    print(type(y))
    y = int(y)

    for i in range(y):
        print(name)

    z = 20
    z = float(z)
    print(z)
    z = 20.54345677
    #can round to a certain number of decimal places
    print(round(z, 3))
    print(round(z, 0))


    #Lists! Each list is a collection of elements in a specific order (position)
    L = [2.5, "Frank", True, 0, 23, x]
    for element in L:
        print(element)

    print(L[0])
    print(L[3:])

    #calling methods
    #NEED ()

    #no return
    Junha()

    #return

    n, name3 = Khang()
    print(n)
    print(name3)
    print(Khang())

    print(CentralTendencies(3, 5, 5))

    
    




    



if __name__ == "__main__":
    main()
