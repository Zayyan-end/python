import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())
        si = (p * r * t) / 100
        result_var.set(f"Simple Interest: ${si:.2f}")
    except ValueError:
        result_var.set("Please enter valid numbers.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x250")

tk.Label(root, text="Principal ($):").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Rate (% per year):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Time (years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold")).pack()

root.mainloop()
