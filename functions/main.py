from add import *
from deposit import  *
from transactions import *
from send_email import *

from PIL import Image,ImageTk



root = Tk()
root.geometry("1250x650+100+40")
root.config(bg = "silver")
root.resizable(False,False)

im = Image.open("/home/wael/Downloads/transactions.jpg")
img = ImageTk.PhotoImage(im)

im_employee = Image.open("/home/wael/Downloads/employee.jpg")
img2 = ImageTk.PhotoImage(im_employee)

menu = Menu(root,bd = 2,relief = "groove")
sub = Menu(menu,tearoff = 0)

menu.add_cascade(label = "View",menu = sub)
sub.add_command(label = "Accounts")

menu.add_command(label = "Transactions",command=transactions)

root.configure(menu= menu)

title = Label(root,text = "The Islamic Bank",padx = 80,pady = 8,bg = "silver",fg = "#17202a",
              font = "Arial 22",bd = 2,relief = "groove")
title.place(x = 420,y = 16)

noteStyle = ttk.Style()
noteStyle.theme_use('alt')
noteStyle.configure("TNotebook", background="silver")
noteStyle.map("TNotebook", background=[("selected", "silver")])

my_note = ttk.Notebook(root)
my_note.place(x = 60,y = 70)

frame = Frame(root,bg = "silver",width = 60,height = 512,bd = 1,relief = "groove")
frame.place(x = 0,y = 130)

fram1 = Frame(my_note,bg = "silver",width = 1180,height = 550)
fram1.place(x = 10,y = 70)

fram2 = Frame(my_note,bg = "silver",width = 1180,height = 550)
fram2.place(x = 10,y = 70)

fram3 = Frame(my_note,bg = "silver",width = 1180,height = 550)
fram3.place(x = 10,y = 70)

fram4 = Frame(my_note,bg = "silver",width = 1180,height = 550)
fram4.place(x = 10,y = 70)

my_note.add(fram1,text = "Create Account")
my_note.add(fram2,text = "Deposit")
my_note.add(fram3,text = "Withdraw")
my_note.add(fram4,text = "Customer list")

t_b = Button(frame,image = img,bd = 0,command=transactions)
t_b.place(x = 7,y = 10)

e_b = Button(frame,image = img2,bd = 0)
e_b.place(x = 7,y = 80)

add_label(fram1)
customer_list(fram4)
deposit(fram2)

mainloop()