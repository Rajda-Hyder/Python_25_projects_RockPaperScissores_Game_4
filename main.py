import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.withdraw()  # Yeh window hide kar dega
color = colorchooser.askcolor()[1]  # Color picker open hoga
print(f"Selected Color: {color}")  # Jo color choose kiya, uska HEX code print hoga
