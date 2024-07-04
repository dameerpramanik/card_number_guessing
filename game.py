from cards import card_1, card_2, card_3, card_4, card_5

def game():
    #initalise the result
    result = 0
    #show card_1
    card_1()
    answer = input("Is your number on this card? (y/n):\n").lower()
    if answer == "y":
        result = result + 1
    #show card_2
    card_2()
    answer = input("Is your number on this card? (y/n):\n").lower()
    if answer == "y":
        result = result + 2
    #show card_3
    card_3()
    answer = input("Is your number on this card? (y/n):\n").lower()
    if answer == "y":
        result = result + 4
    #show card_4
    card_4()
    answer = input("Is your number on this card? (y/n):\n").lower()
    if answer == "y":
        result = result + 8 
    #show card_5
    card_5()
    answer = input("Is your number on this card? (y/n):\n").lower()
    if answer == "y":
        result = result + 16
    #show result
    print("The number you were thinking of is:")
    print(result)