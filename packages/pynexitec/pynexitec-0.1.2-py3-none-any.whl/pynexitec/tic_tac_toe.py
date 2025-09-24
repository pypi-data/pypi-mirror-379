import random

def print_board(board):
    """Prints the board as a dynamic box grid"""
    print()
    for i in range(3):
        row = " | ".join(board[i])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board, player):
    """Returns True if the player has won"""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    """Get player input and validate"""
    while True:
        move = input("Enter your move (row,col: 1-3,1-3): ")
        try:
            row, col = map(int, move.split(","))
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            return row, col
        except (ValueError, IndexError):
            print("Invalid input! Use format row,col like 1,3")

def computer_move(board):
    """Simple AI: random empty cell"""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def play_tic_tac_toe():
    """Main game function"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe by Pynexitec!")
    print("You are X, computer is O")
    print_board(board)

    while True:
        # Player move
        row, col = player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        if is_draw(board):
            print("It's a draw! 🤝")
            break

        # Computer move
        print("Computer is making a move...")
        row, col = computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! 💻")
            break
        if is_draw(board):
            print("It's a draw! 🤝")
            break
