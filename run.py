"""This module implements a simple battleship game."""
from random import randint

# Main board for displaying ships
CONCEALED_BOARD = [[" "] * 6 for x in range(6)]
# Displays if its a hit or a miss
USER_BOARD = [[" "] * 6 for i in range(6)]


def print_board(board):
    print("  A B C D E F  ")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, }


# The computer creates 5 ships within the board
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    """
    Prompt the user to enter the row and column of the battleship location.

    Returns:
        tuple: A tuple containing the row (int) and column (int) indices.
    """
    row = input("Enter the row of the battleship: ").upper()
    while row not in "123456" or row == "":
        print('Not a valid choice, please select a valid row')
        row = input("Enter the row of the battleship: ").upper()
    column = input("Enter the column of the battleship: ").upper()
    while column not in "ABCDEF" or column == "":
        print('Not a valid choice, please select a valid column')
        column = input("Enter the column of the battleship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# checks if it was hit or a miss
def count_hit_ships(board):
    """
    Prompts the user to enter the row and column of the battleship location.

    Returns:
        tuple: A tuple containing the row (int) and column (int) indices.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    create_ships(CONCEALED_BOARD)
    turns = 15
    while turns > 0:
        print('Guess a battleship location')
        print_board(USER_BOARD)
        row, column = get_ship_location()
        if USER_BOARD[row][column] == "-":
            print("You already guessed that one!")
        elif CONCEALED_BOARD[row][column] == "X":
            print("Hit")
            USER_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            USER_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(USER_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left!")
        if turns == 0:
            print("No more turns!\n")
