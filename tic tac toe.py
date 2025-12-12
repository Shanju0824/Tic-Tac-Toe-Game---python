import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game state variables
player = "X"
board = [""] * 9
buttons = []

# Function to check for winner
def check_winner():
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return True
    return False

def is_draw():
    return all(cell != "" for cell in board)

# Function to handle button clicks
def on_click(i):
    global player
    if board[i] == "":
        board[i] = player
        buttons[i].config(text=player, state="disabled")

        if check_winner():
            messagebox.showinfo("Game Over", f"🎉 Player {player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

# Function to reset the game
def reset_game():
    global player, board
    player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", state="normal")

# Create 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 32), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the app
root.mainloop()
