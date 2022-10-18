from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
from mysql import connector

global my_tree
def add_label(master):

    columns = ["First Name", "Last Name", "Nationality", "Gender", "Address", "Account No", "Email", "State",
               "Account type"]
    gen_var = StringVar()
    gen_var.set("Male")

    acc_t_var = StringVar()

    l_title = Label(master, text="Create New Account", bg="silver", font="Arial 22",
                    bd=1, relief="raised")
    l_title.place(x=1, y=3)

    cr_acc = Frame(master, width=1180, bg="silver")
    cr_acc.place(x=30, y=100)

    l_1 = Label(cr_acc, text="First Name", bg="silver")
    l_1.grid(row=0, column=0)

    en_1 = Entry(cr_acc, borderwidth=3)
    en_1.grid(row=0, column=1, ipadx=40, ipady=5)

    l_2 = Label(cr_acc, text="Last Name", padx=30, bg="silver")
    l_2.grid(row=1, column=0)

    en_2 = Entry(cr_acc, borderwidth=3)
    en_2.grid(row=1, column=1, ipadx=40, ipady=5)

    l_3 = Label(cr_acc, text="Nationality", padx=30, bg="silver")
    l_3.grid(row=2, column=0)

    en_3 = Entry(cr_acc, borderwidth=3)
    en_3.grid(row=2, column=1, ipadx=40, ipady=5)

    l_4 = Label(cr_acc, text="Gender", padx=30, bg="silver")
    l_4.grid(row=0, column=2)

    Radiobutton(cr_acc, text="Male", bg="silver", bd=0, variable=gen_var, value="Male").grid(row=0,
                                                                                             column=2,
                                                                                             columnspan=2)
    Radiobutton(cr_acc, text="Female", bg="silver", bd=0, variable=gen_var, value="Female").grid(row=0,
                                                                                                 column=3,
                                                                                                 )

    l_5 = Label(cr_acc, text="Address", padx=30, bg="silver")
    l_5.grid(row=1, column=2)

    en_5 = Entry(cr_acc, borderwidth=3)
    en_5.grid(row=1, column=3, ipadx=40, ipady=5)

    l_6 = Label(cr_acc, text="Account No.", padx=30, bg="silver")
    l_6.grid(row=2, column=2)

    en_6 = Entry(cr_acc, borderwidth=3)
    en_6.grid(row=2, column=3, ipadx=40, ipady=5)

    l_7 = Label(cr_acc, text="Email", padx=30, bg="silver")
    l_7.grid(row=0, column=4)

    en_7 = Entry(cr_acc, borderwidth=3)
    en_7.grid(row=0, column=5, ipadx=40, ipady=5)

    l_8 = Label(cr_acc, text="State", padx=30, bg="silver")
    l_8.grid(row=1, column=4)

    en_8 = Entry(cr_acc, borderwidth=3)
    en_8.grid(row=1, column=5, ipadx=40, ipady=5)

    l_9 = Label(cr_acc, text="Acoount Type", padx=30, bg="silver")
    l_9.grid(row=2, column=4)

    act_op = OptionMenu(cr_acc, acc_t_var, "Savings Accounts", "Current Account", "Checking Accounts")
    act_op.grid(row=2, column=5, ipadx=60)

    acc_t_var.set("Savings Accounts")
    act_op.config(width=7)

    sc = Scrollbar(master)
    sc.place(height=250, x=1160, y=290)
    my_tree: Treeview = ttk.Treeview(master, yscrollcommand=sc.set)
    style = ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview", background="silver", fieldbackground="silver")
    style.map("Treeview", background=[("selected", "green")])

    my_tree["columns"] = [i for i in columns]
    my_tree["show"] = "headings"

    for x in columns:
        my_tree.heading(x, text=x)

    my_tree.column(columns[0], width=127)
    my_tree.column(columns[1], width=117)
    my_tree.column(columns[2], width=124)
    my_tree.column(columns[3], width=80)
    my_tree.column(columns[4], width=129)
    my_tree.column(columns[5], width=123)
    my_tree.column(columns[6], width=197)
    my_tree.column(columns[7], width=117)
    my_tree.column(columns[8], width=127)

    db = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
    cr = db.cursor()

    cr.execute('''SELECT * FROM info''')
    rows = [i for i in cr.fetchall()]

    db.close()

    for x in rows:
        my_tree.insert("", "end", values=x)

    my_tree.place(width=1150, height=250, x=10, y=290)
    sc.config(command=my_tree.yview)

    def act_add():

        if en_1.get() != "" and en_2.get() != "" and en_3.get() != "" and en_5.get() != "" and en_6.get() != "" and en_7.get() != "" and en_8.get() != "":
            val = [en_1.get(), en_2.get(), en_3.get(), gen_var.get(), en_5.get(),
                   int(en_6.get()), en_7.get(), en_8.get(), acc_t_var.get(), 0]

            my_tree.insert("", "end", values=val)
            #my_tree2.insert("", "end", values=val)

            db = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
            cr = db.cursor()

            sql = ('''INSERT INTO info (First_Name,Last_Name,
                                        Nationality,Gender,Address
                                        ,Account_No,Caste,State,
                                        Account_type,balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
            cr.execute(sql, val)

            db.commit()
            db.close()

            en_1.delete(0, END)
            en_2.delete(0, END)
            en_3.delete(0, END)
            en_5.delete(0, END)
            en_6.delete(0, END)
            en_7.delete(0, END)
            en_8.delete(0, END)

        else:
            messagebox.showerror("Error", "Check All fields!")

    b = Button(master, text="Add", bg="silver", padx=100, pady=11, bd=3, relief="groove", command=act_add)
    b.place(x=480, y=230)

