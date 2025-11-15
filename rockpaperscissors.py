import tkinter as tk
import random

def play(choice):
    cpu = random.choice(["Rock", "Paper", "Scissors"])
    if choice == cpu:
        result = "Tie"
    elif (choice == "Rock" and cpu == "Scissors") or \
         (choice == "Paper" and cpu == "Rock") or \
         (choice == "Scissors" and cpu == "Paper"):
        result = "You Win"
    else:
        result = "CPU Wins"
    label.config(text=f"You: {choice}\nCPU: {cpu}\n{result}")

root = tk.Tk()
root.title("RPS")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
label.pack()

for c in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=c, command=lambda ch=c: play(ch)).pack()

root.mainloop()
