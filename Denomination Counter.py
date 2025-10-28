from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title('Denomination counter')

root.configure(bg= 'light blue')
root.geometry('650x400')


upload = Image.open('C://Users//Owner//Downloads//app_img.jpg')
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image,bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text='Hey user! Welcome to the Dnomination Counter Application.',
               bg='light blue'
               )
label1.place(rel=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        'Alert', 'Do you want to calculate Denomination count?'
    )
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,
                 text='Lets get started!',
                 command=msg,
                 bg='brown',
                 
                 fg='white'
                 )
button1.place(x=260, y=360)

def topwin():
    top= Toplevel()
    top.title('Denominations Calculator')
    top.configure(bg='light gray')
    top.geometry('600x350+50+50')

    Label=label(top, text='Enter total amount', bg='light grey')
    entry=Entry(top)
    lbl=label(top, text= 'Here are the number notes for each denomintion', bg='light grey')
    l1= Label(top, text='50'bg='light grey')

    l2= Label(top, text='20'bg='light grey')

    l3= Label(top, text='10'bg='light grey')

    l4= Label(top, text='5'bg='light grey')

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)

    def calulator():