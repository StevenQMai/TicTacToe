from tkinter import * 
import random

def next_turn(row, column):
    global player
    # Ensure the space is empty and no winner has been determined yet
    if buttons[row][column]["text"] == "" and check_winner() is False:
        
        # Update the button with the current player's symbol
        buttons[row][column]["text"] = player

        # Check if the game is won, tied, or should continue
        if check_winner() is False:
            # Switch player turn
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + "'s turn"))
        
        elif check_winner() is True:
            # If there is a winner, display the winner's message and stop further moves
            label.config(text=(player + " wins"))
            disable_buttons()

        elif check_winner() == "Tie":
            # If it's a tie, display tie message and stop further moves
            label.config(text="Tie!")
            disable_buttons()

def disable_buttons():
    #Disables all buttons once the game is over (either win or tie).
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=DISABLED)

def enable_buttons():
    #Enables all buttons for a new game.
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=NORMAL)

def check_winner():
    # Check horizontal win conditions
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    # Check vertical win conditions
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonal win conditions
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # If no win and no empty spaces, it's a tie
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    # If no winner yet and spaces are still available
    else:
        return False

def empty_spaces():
    #Checks if there are any empty spaces left on the board.
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    #Resets the game state to start a new game
    global player
    player = random.choice(players)
    label.config(text = player + "'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = "#F0F0F0")
    enable_buttons()

# Set up the main window
window = Tk() 
window.title("Tic-Tac-Toe!")

players = ["x", "o"]
player = random.choice(players)

# Create the grid of buttons
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Display the player's turn
label = Label(text=player + "'s turn", font=('times', 40))
label.pack(side="top")

# Restart game button
reset_button = Button(text="restart", font=("times", 20), command=new_game)
reset_button.pack(side="top")

# Frame to hold the buttons (the Tic-Tac-Toe grid)
frame = Frame(window)
frame.pack()

# Create the buttons for the grid and add them to the frame
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('times', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter loop
window.mainloop()
