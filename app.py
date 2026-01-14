import tkinter as tk
from tkinter import messagebox

# ---------- Functions ----------
def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not game_over[0]:
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            game_over[0] = True
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over[0] = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"{current_player}'s turn")

def check_winner(player):
    # Check rows
    for row in buttons:
        if all(btn["text"] == player for btn in row):
            return True
    # Check columns
    for col in range(3):
        if all(buttons[row][col]["text"] == player for row in range(3)):
            return True
    # Check diagonals
    if all(buttons[i][i]["text"] == player for i in range(3)):
        return True
    if all(buttons[i][2-i]["text"] == player for i in range(3)):
        return True
    return False

def is_draw():
    return all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

def retry_game():
    global current_player
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    current_player = "X"
    label.config(text=f"{current_player}'s turn")
    game_over[0] = False

# ---------- Main Window ----------
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x450")
root.resizable(False, False)

current_player = "X"
game_over = [False]  # use list to make it mutable in inner function

# Label for turn
label = tk.Label(root, text=f"{current_player}'s turn", font=("Arial", 16))
label.pack(pady=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

buttons = []
for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda row=r, col=c: button_click(row, col))
        btn.grid(row=r, column=c)
        row.append(btn)
    buttons.append(row)

# Retry Button
retry_btn = tk.Button(root, text="Retry", font=("Arial", 14), command=retry_game)
retry_btn.pack(pady=10)

# Quit Button
quit_btn = tk.Button(root, text="Quit", font=("Arial", 14), command=root.destroy)
quit_btn.pack(pady=5)

# Run the app
root.mainloop()
