# --- TIC TAC TOE GAME ---
# Player = X
# AI = O

# Empty board
board = [" " for _ in range(9)]

# Print game board
def print_board():
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---+---+---")
    print()

# Handle player's move
def player_move():
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("❌ Please choose a number between 1 and 9!")
            elif board[move] != " ":
                print("❌ That spot is already taken. Try again!")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("❌ Numbers only! Example: 1, 2, 3 ...")

# Simple AI move (chooses first empty space)
def ai_move():
    print("AI is thinking...\n")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

# Check win
def check_win(player):
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_patterns)

# Check tie
def check_tie():
    return " " not in board

# --- GAME LOOP ---
print("\n🎮 Welcome to Tic Tac Toe!")
print("You are X, AI is O.\n")

while True:
    print_board()
    player_move()

    if check_win("X"):
        print_board()
        print("🎉 You win! Great job!")
        break

    if check_tie():
        print_board()
        print("🤝 It's a tie!")
        break

    ai_move()

    if check_win("O"):
        print_board()
        print("💻 AI wins! Better luck next time!")
        break

    if check_tie():
        print_board()
        print("🤝 It's a tie!")
        break
3