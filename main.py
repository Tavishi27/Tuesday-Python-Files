# Global Variables
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
player = "X"


def print_board():
    heading = ["", "0", "1", "2"]
    line = ""
    for item in heading:
        line += item + "\t"
    print(line + "\n")

    for n in range(0, len(board)):
        line = str(n) + "\t"
        for i in range(0, len(board[n])):
            line += board[n][i] + "\t"
        print(line + "\n")


# returns true if a row,col on the board is open
def is_valid_move(row, col):
    return row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == "-"


# places player on row,col on the board
def place_player(player, row, col):
    board[row][col] = player


# Asks the user to enter a row and col until the user enters a valid location
# Adds user location to the board, and prints the board
def take_turn(player):
    if player == "X":
        row = int(input("Enter a row: "))
        col = int(input("Enter a col: "))
        while not (is_valid_move(row, col)):
            print("Please enter a valid move")
            row = int(input("Enter a row: "))
            col = int(input("Enter a col: "))
    else:
        score, row, col = minimax("O")
    place_player(player, row, col)
    print_board()


# Write your check win functions here:
# returns true if player has won in any of the three columns.
# A player wins if they have three consecutive X's or O's in a column.
def check_col_win(player):
    for n in range(0, len(board)):
        col_data = ""
        for i in range(0, len(board)):
            col_data += board[i][n]
        if col_data == (player + player + player):
            return True
    return False


# returns true if player has won in any of the three row.
# A player wins if they have three consecutive X's or O's in a row.
def check_row_win(player):
    for n in range(0, len(board)):
        row_data = ""
        for i in range(0, len(board)):
            row_data += board[n][i]
        if row_data == (player + player + player):
            return True
    return False


# returns true if player has won in either diagonal directions.
# A player wins if they have three consecutive X's or O's in a diagonal.
def check_diag_win(player):
    diag_data = ""
    for n in range(0, len(board)):
        diag_data += board[n][n]
    if diag_data == (player + player + player):
        return True
    diag_data = ""
    for n in range(0, len(board)):
        diag_data += board[n][len(board[0]) - 1 - n]
    if diag_data == (player + player + player):
        return True
    return False


# returns true if player has won the game.
def check_win(player):
    return check_col_win(player) or check_row_win(player) or check_diag_win(player)


# returns true if all spots on the board have been taken, and there is no winner.
def check_tie():
    for row in board:
        for col in row:
            if col == "-":
                return False
    X_has_won = check_win("X")
    O_has_won = check_win("O")
    return not (X_has_won and O_has_won)


def minimax(player):
    # base case
    if check_win("O"):
        return (10, None, None)
    elif check_win("X"):
        return (-10, None, None)
    elif check_tie():
        return (0, None, None)

    # recursive case
    # best means best for the computer
    # worst means worst for the computer
    if player == "O":
        best = -10000
        best_move = []
        for row in range(0, len(board)):
            for col in range(0, len(board)):
                if is_valid_move(row, col):
                    place_player("O", row, col)
                    value = minimax("X")[0]
                    if value > best:
                        best = value
                        best_move = [row, col]
                    place_player("-", row, col)
        return (best, best_move[0], best_move[1])

    if player == "X":
        worst = 10000
        worst_move = []
        for row in range(0, len(board)):
            for col in range(0, len(board)):
                if is_valid_move(row, col):
                    place_player("X", row, col)
                    value = minimax("O")[0]
                    if value < worst:
                        worst = value
                        worst_move = [row, col]
                    place_player("-", row, col)
        return (worst, worst_move[0], worst_move[1])


# Start of program
print("Welcome to Tic Tac Toe!")
print_board()

game_is_active = True
while game_is_active:
    print(player + "'s turn:")
    take_turn(player)
    if check_win(player):
        print(player + " wins!")
        game_is_active = False
    if check_tie():
        print("It's a tie")
        game_is_active = False
    if player == "X":
        player = "O"
    else:
        player = "X"