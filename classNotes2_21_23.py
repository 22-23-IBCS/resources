def CShello():
    name = input("Give a name\n")
    return "Hello, " + name + ". Welcome to Computer Science Class."

def main():

    sample = open("sampleText.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word = word.lower()
        if "ad" in word:
            print(word)













    '''print(CShello())

    # String formatting
    # Create place-holders for various strings and "fields"
    # print things with the place-holders substiting different values

    name = "Mr. Considine"
    greeting = "Hello, {}. Welcome to Computer Science Class."
    # change place-holder with the value of name
    print(greeting.format(name))

    name = "Frank"
    print(greeting.format(name))

    text = "Whoah, a {2}, you did amazingly, {0} on the final exam! Thanks, {1}"
    name = "Mr. Phillips"
    grade = 99
    print(text.format(name, "Finn", grade))

    # Can also format integers and floats
    price = 134.6799999
    txt = "Yikes, gas costs ${:2f} a gallon!"
    print(txt.format(price))'''

    


if __name__ == "__main__":
    main()
