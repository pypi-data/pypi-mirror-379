# tic_tac_toe.py

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(board, player):
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

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe by Pynexitec!")
    print_board(board)

    while True:
        player = players[turn % 2]
        move = input(f"Player {player}, enter your move (row,col: 1-3,1-3): ")
        try:
            row, col = map(int, move.split(","))
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Cell already taken, try again.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Invalid input, use row,col like 1,3")
            continue

        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins! 🎉")
            break
        if is_draw(board):
            print("It's a draw! 🤝")
            break

        turn += 1
