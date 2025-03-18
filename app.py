import tkinter as tk
import random

# Function to determine the winner
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 😢"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

# Add a Label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14 , "bold"),bg = "#ffd9ff" , fg ="#54a800")
label.pack(pady=20)

# Add Buttons
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock 🌑", font=("Arial", 12),bg = "#ffd5d5", fg = "#1a1aff", command=lambda: play("Rock"))
rock_button.pack(side="left", padx=10)

paper_button = tk.Button(button_frame, text="Paper 📄", font=("Arial", 12),bg = "#ffd5d5", fg = "#1a1aff", command=lambda: play("Paper"))
paper_button.pack(side="left", padx=10)

scissors_button = tk.Button(button_frame, text="Scissors ✂️", font=("Arial", 12),bg = "#ffd5d5", fg = "#1a1aff", command=lambda: play("Scissors"))
scissors_button.pack(side="left", padx=10)

# Add Result Label
result_label = tk.Label(root, text="", font=("Arial", 12),bg = "#c1ffff",fg = "#e60000")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
