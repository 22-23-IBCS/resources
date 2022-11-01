def main():

    # dictionaries are a set in that they have no order and unique items
    # a set of key : value
    #rating 0-5
    '''candy = {"Snickers" : 3,
             "Reese's" : 5,
             "Twix" : 4,
             "Nerds" : 1,
             "Hershey's" : 1,
             "Kit-kat" : 2,
             "M&M's" : 1,
             "Peanut M&M's" : 4,
             "Almond Joy" : 0}

    #print(candy)

    #items in the dictionary are accessed based off their key

    print(candy.get("Twizlers"))
    candy.update({"Twizlers" : 1})
    print(candy.get("Twizlers"))
    keys = list(candy.keys())
    for k in keys:
        print(k)

    print(candy.get(5))'''


    #Food store

    food = {"Pasta" : 4.50,
             "Pizza" : 5.75,
             "Hot-Pocket" : 3.00,
             "Soup" : 4.50,
             "Russet Potato" : 0.75}

    '''print(list(food.keys()))
    request = input("What food would you like to buy?\n")
    price = food.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go!\nYou got " + str(many) + " " + request)
    print("That would be $" + str(round(price*many, 2)) + " dollars")'''

    toBuy = []
    while True:
        res = input("What would you like to buy? Enter 'stop' if done\n")
        if res == "stop":
            break
        else:
            toBuy.append(res)

    print(toBuy)
    
    





    


if __name__ == "__main__":
    main()
