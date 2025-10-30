import tkinter as tk

def check_password():
    pwd = entry.get()
    if len(pwd) < 8:
        result.set("Too short ❌")
    elif any(char.isdigit() for char in pwd):
        result.set("Looks good ✅")
    else:
        result.set("Add a number ⚠️")

root = tk.Tk()
root.title("Password Checker")

tk.Label(root, text="Enter password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Check", command=check_password).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
