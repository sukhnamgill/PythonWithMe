import math

# Initial board
board = [['' for _ in range(3)] for _ in range(3)]

# Winning combinations
winning = [[(0, 0), (0, 1), (0, 2)],
           [(1, 0), (1, 1), (1, 2)],
           [(2, 0), (2, 1), (2, 2)],
           [(0, 0), (1, 0), (2, 0)],
           [(0, 1), (1, 1), (2, 1)],
           [(0, 2), (1, 2), (2, 2)],
           [(0, 0), (1, 1), (2, 2)],
           [(0, 2), (1, 1), (2, 0)]]

# Function to display board
def print_board(b):
    for row in b:
        print(" | ".join(cell if cell != '' else ' ' for cell in row))
        print("-" * 9)

# Check if a player has won
def who_won(b, player):
    player_positions = [(i, j) for i in range(3) for j in range(3) if b[i][j] == player]
    for combo in winning:
        if all(pos in player_positions for pos in combo):
            return True
    return False

# Check board status
def check(b):
    if who_won(b, "X"):
        return 1
    elif who_won(b, "O"):
        return -1
    elif all(b[i][j] != '' for i in range(3) for j in range(3)):
        return 0
    return None

# Minimax function
def minimax(b, tf):
    result = check(b)
    if result is not None:
        return result

    if tf:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = "X"
                    score = minimax(b, False)
                    b[i][j] = ""
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = "O"
                    score = minimax(b, True)
                    b[i][j] = ""
                    best_score = min(best_score, score)
                    
        return best_score

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = minimax(board, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = "X"
    print(f"\nAI chose position ({move[0]}, {move[1]})")

# Human move
def human_move():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] == "":
                board[row][col] = "O"
                break
            else:
                print("Cell already taken!")
        except (IndexError, ValueError):
            print("Invalid input! Try again.")

# Main game loop
print("Welcome to Tic Tac Toe!")
print("You are 'O'. AI is 'X'.")
print_board(board)

while True:
    # Human turn
    human_move()
    print_board(board)
    result = check(board)
    if result is not None:
        break

    # AI turn
    ai_move()
    print_board(board)
    result = check(board)
    if result is not None:
        break

# Result
if result == 1:
    print("AI (X) wins! 🤖")
elif result == -1:
    print("You (O) win! 🎉")
else:
    print("It's a draw! 🤝")
