import random

def create_shuffeled_deck():
    global deck
    cards = ["A", "B"]
    deck = cards * 2
    random.shuffle(deck)
    return (deck)

def play_round():
    max_index = len(deck) - 1
    while "*" in display_deck:
        first_guess = int(input(f'select an index from 0-{max_index} : '))
        display_deck[first_guess] = deck[first_guess]
        print('Deck: ', display_deck)
        
        second_guess = int(input(f'select a different index from 0-{max_index} : '))
        display_deck[second_guess] = deck[second_guess]
        print('Deck: ', display_deck)

        if deck[first_guess] != deck[second_guess] :
            print("ohhh.. try again.")
            display_deck[first_guess] = "*"
            display_deck[second_guess] = "*"
        else:
            print("you found a couple! nice! go on like this!")


    print ("great job! game is over! do you want to play again?")


if __name__ == "__main__":

        print("welcome to the memory game!")
        while True:
            new_game = input ("press R to start playing, or Q to quit. ").upper()
            if new_game == "R" :
                create_shuffeled_deck()
                display_deck = ["*"] * len(deck)
                print("Deck: ", display_deck)
                play_round()

            elif new_game != "R":
                print ("goodbye then.\n see you next time :)")
                break
