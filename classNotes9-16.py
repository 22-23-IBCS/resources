def main():
    
    name = input("What is your name?\n")

    print("Hello, " + name + "!")

    age = int(input("How old are you?\n"))

    age = age + 10

    print(age)
    print("Wow. Old! " + str(age))

if __name__ == "__main__":
    main()
