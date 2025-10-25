import tkinter as tk
def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm=inches*2.54
        result_label.config(text=f'{cm:.2f}cm')
    except ValueError:
        result_label.config(text='Please enter a valid number')
root=tk.Tk()
root.title('Inches to Centimeters Converter')
root.geometry('300x200')
label = tk.Label(root,text='enter length in inches',font=('Arial', 12))
label.pack(pady=10)
entry_inch=tk.Entry(root, font=('Ariel',12))
entry_inch.pack(pady=5)
convert_button=tk.Button(root,text='Convert',command=convert_to_cm,font=('Arial',12),bg='lightblue')
convert_button.pack(pady=10)
result_label=tk.Label(root, text='', font=('Arial',12, 'bold'))
result_label.pack(pady=10)
root.mainloop()