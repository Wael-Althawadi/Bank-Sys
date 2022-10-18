from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql import connector
from add import *
from PIL import Image,ImageTk



def customer_list(master):
    global my_tree2
    global img
    global img_upt

    columns = ["First Name", "Last Name", "Nationality", "Gender", "Address", "Account No", "Email", "State",
               "Account type", "balance"]

    gen_var = StringVar()
    gen_var.set("Male")

    im = Image.open("/home/wael/Downloads/delete-icon.jpg")
    img = ImageTk.PhotoImage(im)

    im2 = Image.open("/home/wael/Downloads/update-icon.jpg")
    img_upt = ImageTk.PhotoImage(im2)


    acc_t_var = StringVar()

    c_title = Label(master, text="Mange Accounts", bg="silver", font="Arial 22",
                    bd=1, relief="raised")
    c_title.place(x=1, y=3)

    cu_acc = Frame(master, width=700, bg="silver")
    cu_acc.place(x=300, y=100)

    b_frame = Frame(master, width=270, height=225, bg="silver", bd=1, relief="solid")
    b_frame.place(x=10, y=50)

    l_1 = Label(cu_acc, text="First Name", bg="silver")
    l_1.grid(row=0, column=0)

    en_1 = Entry(cu_acc, borderwidth=3)
    en_1.grid(row=0, column=1, ipadx=40, ipady=5)

    l_2 = Label(cu_acc, text="Last Name", padx=30, bg="silver")
    l_2.grid(row=1, column=0)

    en_2 = Entry(cu_acc, borderwidth=3)
    en_2.grid(row=1, column=1, ipadx=40, ipady=5)

    l_3 = Label(cu_acc, text="Nationality", padx=30, bg="silver")
    l_3.grid(row=2, column=0)

    en_3 = Entry(cu_acc, borderwidth=3)
    en_3.grid(row=2, column=1, ipadx=40, ipady=5)

    l_7 = Label(cu_acc, text="Email", padx=30, bg="silver")
    l_7.grid(row=0, column=2)

    en_7 = Entry(cu_acc, borderwidth=3)
    en_7.grid(row=0, column=3, ipadx=40, ipady=5)

    l_5 = Label(cu_acc, text="Address", padx=30, bg="silver")
    l_5.grid(row=1, column=2)

    en_5 = Entry(cu_acc, borderwidth=3)
    en_5.grid(row=1, column=3, ipadx=40, ipady=5)

    l_8 = Label(cu_acc, text="State", padx=30, bg="silver")
    l_8.grid(row=2, column=2)

    en_8 = Entry(cu_acc, borderwidth=3)
    en_8.grid(row=2, column=3, ipadx=40, ipady=5)

    l_6 = Label(cu_acc, text="Account No.", padx=30, bg="silver")
    l_6.grid(row=5, column=0)

    en_6 = Entry(cu_acc, borderwidth=3)
    en_6.grid(row=5, column=1, ipadx=40, ipady=5)

    l_9 = Label(cu_acc, text="Acoount Type", padx=30, bg="silver")
    l_9.grid(row=5, column=2, rowspan=2)

    act_op = OptionMenu(cu_acc, acc_t_var, "Savings Accounts", "Current Account", "Checking Accounts")
    act_op.grid(row=5, column=3, ipadx=60)

    l_4 = Label(master, text="Gender", padx=30, bg="silver")
    l_4.place(x=315, y=230)

    Radiobutton(master, text="Male", bg="silver", bd=0, variable=gen_var, value="Male").place(x=470, y=230)

    Radiobutton(master, text="Female", bg="silver", bd=0, variable=gen_var, value="Female").place(x=550, y=230)

    acc_t_var.set("Savings Accounts")
    act_op.config(width=7)

    sc2 = Scrollbar(master)
    sc2.place(height=250, x=1160, y=290)

    my_tree2 = ttk.Treeview(master, yscrollcommand=sc2.set)
    style = ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview", background="silver", fieldbackground="silver")
    style.map("Treeview", background=[("selected", "green")])

    my_tree2["columns"] = [i for i in columns]
    my_tree2["show"] = "headings"

    for x in columns:
        my_tree2.heading(x, text=x)

    my_tree2.column(columns[0], width=97)
    my_tree2.column(columns[1], width=97)
    my_tree2.column(columns[2], width=94)
    my_tree2.column(columns[3], width=80)
    my_tree2.column(columns[4], width=119)
    my_tree2.column(columns[5], width=113)
    my_tree2.column(columns[6], width=197)
    my_tree2.column(columns[7], width=97)
    my_tree2.column(columns[8], width=137)
    my_tree2.column(columns[9], width=110)

    db = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
    cr = db.cursor()

    cr.execute('''SELECT * FROM info''')
    rows = [i for i in cr.fetchall()]

    db.close()

    for x in rows:
        my_tree2.insert("", "end", values=x)

    my_tree2.place(width=1150, height=250, x=10, y=290)
    sc2.config(command=my_tree2.yview)

    def del_f():
        en_1.delete(0, END)
        en_2.delete(0, END)
        en_3.delete(0, END)
        en_7.delete(0, END)
        en_5.delete(0, END)
        en_6.delete(0, END)
        en_8.delete(0, END)

    def cliker(e):
        global items

        selected = my_tree2.focus()
        items = my_tree2.item(selected, "values")

        del_f()

        en_1.insert(0, items[0])
        en_2.insert(0, items[1])
        en_3.insert(0, items[2])
        en_7.insert(0, items[6])
        en_5.insert(0, items[4])
        en_6.insert(0, items[5])
        en_8.insert(0, items[7])
        gen_var.set(items[3])
        acc_t_var.set(items[8])

    my_tree2.bind("<Double-1>", cliker)

    def updt():
        global updt_val

        if en_1.get() != "" and en_2.get() != "" and en_3.get() != "" and en_7.get() != "" and en_5.get() != "" and en_6.get() != "" and en_8.get() != "":
            sel = my_tree2.focus()
            m_r = messagebox.askyesnocancel("Warning", "Are you sure!")
            if m_r == True:

                balance = None
                updt_val = [en_1.get(), en_2.get(), en_3.get(), en_7.get(), en_5.get(), en_8.get(), en_6.get()
                    , gen_var.get(), acc_t_var.get(), en_6.get()]
                selec = my_tree2.focus()

                db_updt = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
                cr_updt = db_updt.cursor()

                sql_balance = f'''SELECT balance FROM info WHERE Account_No = {en_6.get()}'''
                cr_updt.execute(sql_balance)
                balance = cr_updt.fetchall()[0][0]

                sql_upd = '''UPDATE info SET First_Name = %s,
                                            Last_Name = %s,
                                            Nationality = %s ,
                                            Caste = %s ,
                                            Address = %s
                                            ,State = %s ,
                                            Account_No = %s ,
                                            Gender = %s ,
                                            Account_type = %s 
                                            WHERE Account_No = %s '''

                cr_updt.execute(sql_upd, updt_val)

                db_updt.commit()
                db_updt.close()

                my_tree2.item(selec, text="", values=[updt_val[0], updt_val[1], updt_val[2], updt_val[7], updt_val[4],
                                                      updt_val[6], updt_val[3], updt_val[5], updt_val[8],balance])




                messagebox.showinfo("message", "Updated Succesfully")

                del_f()
                my_tree2.selection_remove(sel)
            else:
                my_tree2.selection_remove(sel)
                del_f()
        else:
            messagebox.showerror("Error", "Select account to update!")

    b = Button(b_frame,image=img_upt,bd = 2,relief="groove",command=updt)
    b.place(x=80 ,y=15)

    def del_():
        global s_val

        select = my_tree2.focus()
        s_val = my_tree2.item(select, "values")
        if s_val != "":
            d_m = messagebox.askyesnocancel("Warning", f"Are you sure you want to delete {s_val[0]} Data?")
            if d_m == True:
                db_del = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
                cr_del = db_del.cursor()

                del_sql = f'''DELETE FROM info WHERE Account_No = {s_val[5]}'''
                cr_del.execute(del_sql)
                db_del.commit()
                db_del.close()

                messagebox.showinfo("message", f"{s_val[0]} Data has been deleted!")
                my_tree2.delete(select)
                #my_tree.delete(select)
                del_f()
                my_tree2.selection_remove(select)
            else:
                del_f()
                my_tree2.selection_remove(select)


        else:
            messagebox.showerror("Error", "Select account to delete!")

    b2 = Button(b_frame,image=img,bd = 2,relief="groove",command=del_)
    b2.place(x=80, y=110)

