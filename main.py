from cards import card_1, card_2, card_3, card_4, card_5
from game import game

def main():
    status = "main"

    while status == "main":
        print("######################################")
        print("#------------------------------------#")
        print("#------------------------------------#")
        print("#---THE_NUMBER_GUESSING_TRICK_GAME---#")
        print("#------------------------------------#")
        print("#------------------------------------#")
        print("######################################\n")

        print("************************************")
        print("*THINK OF A NUMBER BETWEEN 1 AND 30*")
        print("*THE COMPUTER WILL BE ABLE TO GUESS*")
        print("*THE NUMBER YOU WERE THINKING OF   *")
        print("************************************\n")

        print("Options:")
        print("    (1) Start Game")
        print("    (2) Show Cards")
        print("    (3) Exit\n")

        print("Choose an option by typing 1, 2 or 3:")
        option = input()
        option = int(option)

        if option == 1:
            status = "game"
            while status == "game":
                game()
                print("Options:")
                print("    (1) Play Again")
                print("    (2) Back\n")
                option = input("Choose an option by typing 1 or 2:")
                option = int(option)
                if option == 1:
                    status = "game"
                else:
                    status = "main"
        elif option == 2:
            status == "view_cards"
            card_1()
            card_2()
            card_3()
            card_4()
            card_5()
            while input("Done? (y/n)\n").lower() == "n":
                status = "view_cards"
            status = "main"
        else:
            exit()

if __name__ == "__main__":
    main()
