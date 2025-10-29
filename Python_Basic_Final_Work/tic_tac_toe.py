import random

board = [[]]

def show_board():
    print("this is your board: ")
    for i, row in enumerate(board):
        print(" | ".join(map(str, row)))
        if i < 2:
            print("--+---+--")


symbols = ["X", "O"]


def get_random_symbol():
    temp_symbols = symbols.copy()
    random.shuffle(temp_symbols)
    return temp_symbols[0]


player_1 = {}
player_2 = {}
current_player = {}
winner = None


def set_player_1():
    player_1["name"] = input("Hello player 1, what is your name? ")
    while True:
        choose_symbol = input("do you want to choose a symbol? \nenter X or O, or press ENTER for random symbol.").capitalize()
        match choose_symbol:
            case "X" | "O":
                player_1["symbol"] = choose_symbol
                break
            case "":
                player_1["symbol"] = get_random_symbol()
                print(f"your symbol is {player_1["symbol"]}")
                break
            case _:
                print("INVALID input.")


def set_player_2_human():
    player_2["name"] = input("Hello player 2, what is your name? ")

    if player_1["symbol"] == symbols[0]:
        player_2["symbol"] = symbols[1]
    else:
        player_2["symbol"] = symbols[0]
    print(f"{player_2["name"]}, your symbol is {player_2["symbol"]}")

def set_player_2_computer():
    if player_1["symbol"] == symbols[0]:
        player_2["symbol"] = symbols[1]
    else:
        player_2["symbol"] = symbols[0]


def set_current_player():
    global current_player
    if player_1["symbol"] == "X":
        current_player = player_1
        print(f'hey {player_1["name"]} you play X.\n you may start the game :)')
    else:
        current_player = player_2
        if is_multiplayer:
            print(f'hi {player_2["name"]} you play X.\n you may start the game :)')
        else:
            print("the computer plays X, it will play first. ")

def print_stars(message):
    print("")
    print("*******************")
    print("")
    print(message)
    print("")
    print("*******************")
    print("")

def next_player():

    global current_player
    if current_player == player_1:
        current_player = player_2
        if is_multiplayer:
            print_stars(f'{current_player["name"]} you are next. ')
    else:
        current_player = player_1
        print_stars(f'{current_player["name"]} you are next. ')


is_multiplayer = bool
def show_main_menu():
    global is_multiplayer
    while True:
        print("What would you like to do? ")
        selected_option = input("press 1 to start SINGLE PLAYER game \npress 2 to start a MULTIPLAYER match: ")
        match selected_option:
            case "1":
                is_multiplayer = False
                break
            case "2":
                is_multiplayer = True
                break
            case _:
                print("your input is INVALID.")
                continue


def generate_computer_input():
    available_spots = []
    for row in board:
        for cell in row:
            if type(cell) is int:
                available_spots.append(cell)

    random.shuffle(available_spots)
    return available_spots[0]

def play_match():
    global board
    global winner
    global current_player

    board =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

    if winner is None:
        set_current_player()
    else:
        current_player = winner
        winner = None


    while True:
        play_turn()
        if is_match_over():
            show_board()
            if winner is not None:
                if is_multiplayer or winner is player_1:
                    print(f"CONGRATULATIONS {winner["name"]}. you are the winner!!")
                else:
                    print("YOU LOSE! HAHAHAHA!")

            else:
                print(f'WOW! you both are awsome! it is a TIE!')
            break

        else:
            next_player()
def is_computers_turn():
    return (current_player == player_2) & (is_multiplayer == False)

def play_turn():
    row_index = None
    column_index = None

    if not is_computers_turn():
        show_board()

    while True:
        if is_computers_turn():
            player_chosen_spot = generate_computer_input()
        else:
            while True:
                try:
                    player_chosen_spot = int(
                        input('Choose a spot on the board- enter a number between 1-9, that is not yet occupied: '))
                except ValueError:
                    print("INVALID input. please enter a NUMBER between 1-9. ")
                    continue

                if not 1 <= player_chosen_spot <= 9:
                    print("INVALID input. please enter a number BETWEEN 1-9. ")
                    continue
                break


        for row in board:
            if player_chosen_spot in row:
                row_index = board.index(row)
                column_index = row.index(player_chosen_spot)
                break

        if column_index is not None:
            break
        else:
            print("That spot is already taken — please choose another.")

    board[row_index][column_index] = current_player["symbol"]


def is_match_over():
    global board
    global winner
    # win:
    if (
            (board[0][0] == board[0][1] == board[0][2]) |  # 1st row
            (board[1][0] == board[1][1] == board[1][2]) |  # 2nd row
            (board[2][0] == board[2][1] == board[2][2]) |  # 3rd row

            (board[0][0] == board[1][0] == board[2][0]) |  # 1st col
            (board[0][1] == board[1][1] == board[2][1]) |  # 2nd col
            (board[0][2] == board[1][2] == board[2][2]) |  # 3rd col

            (board[0][0] == board[1][1] == board[2][2] )|  # 1st dia
            (board[0][2] == board[1][1] == board[2][0])  # 2nd dia
    ):
        winner = current_player
        return True

    # tie:
    for raw in board:
        for cell in raw:
            if type(cell) == int:
                return False
    return True


if __name__ == "__main__":
    print("Welcome to the TIC TAC TOE game :) ")
    show_main_menu()
    set_player_1()
    if is_multiplayer == True:
        set_player_2_human()
    else:
        set_player_2_computer()

    # set_current_player()
    # current_player["symbol"] = symbols[0]

    #game
    while True:
        play_match()
        while True:
            is_game_over = input("would you like to play another match? Y/N ").capitalize()
            match is_game_over:
                case "Y":
                    if winner is not None:
                        # current_player = winner
                        print (f'{winner["name"]} you won. now you get to go first :) ')
                    # else:
                    #     set_current_player()
                    break

                case "N":
                    print("thanks for playing. you da best.")
                    exit()

                case _:
                    print("INVALID input. please enter Y or N.")
                    continue

