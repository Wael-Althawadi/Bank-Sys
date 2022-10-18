from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import PIL.Image
from mysql import connector
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from PIL import ImageTk
import PIL.Image

from customer import *
from transactions import *
from send_email import *




def deposit(master):
    global img

    im = PIL.Image.open("/home/wael/Downloads/deposit.jpg")
    img = ImageTk.PhotoImage(im)

    l_img = Label(master,image=img,bd = 0)
    l_img.place(x = 300,y = 0)

    f1_dep = Frame(master, width=240, height=300, bg="silver", bd=1, relief="groove")
    f1_dep.place(x=930, y=130)

    c_title = Label(master, text="Deposit", bg="silver", font="Arial 22",
                    bd=1, relief="raised")
    c_title.place(x=1, y=3)

    f2_dep = Frame(master, width=800, height=450, bg="silver", bd=1, relief="solid")
    f2_dep.place(x=55, y=210)

    f3_dep = Frame(master, width=800, height=230, bg="silver")
    f3_dep.place(x=55, y=360)

    l_d1 = Label(f2_dep, text="First Name", bg="silver")
    l_d1.grid(row=0, column=0)

    ed_1 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_1.grid(row=0, column=1, ipadx=100, ipady=5)

    l_d2 = Label(f2_dep, text="Last Name", padx=30, bg="silver")
    l_d2.grid(row=1, column=0)

    ed_2 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_2.grid(row=1, column=1, ipadx=100, ipady=5)

    l_d3 = Label(f2_dep, text="Nationality", padx=30, bg="silver")
    l_d3.grid(row=2, column=0)

    ed_3 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_3.grid(row=2, column=1, ipadx=100, ipady=5)

    l_d7 = Label(f2_dep, text="Email", padx=30, bg="silver")
    l_d7.grid(row=0, column=2)

    ed_7 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_7.grid(row=0, column=3, ipadx=100, ipady=5)

    l_d5 = Label(f2_dep, text="Address", padx=30, bg="silver")
    l_d5.grid(row=1, column=2)

    ed_5 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_5.grid(row=1, column=3, ipadx=100, ipady=5)

    l_d8 = Label(f2_dep, text="State", padx=30, bg="silver")
    l_d8.grid(row=2, column=2)

    ed_8 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_8.grid(row=2, column=3, ipadx=100, ipady=5)

    l_d6 = Label(f2_dep, text="Account No.", padx=30, bg="silver")
    l_d6.grid(row=5, column=0)

    ed_6 = Label(f2_dep, borderwidth=2, bg="silver", fg="#2c3e50")
    ed_6.grid(row=5, column=1, ipadx=100, ipady=5)

    l_d9 = Label(f2_dep, text="Acoount Type", padx=30, bg="silver")
    l_d9.grid(row=5, column=2)

    act_en = Label(f2_dep, bg="silver", fg="#2c3e50")
    act_en.grid(row=5, column=3, ipadx=100)

    l_d4 = Label(f2_dep, text="Gender", padx=30, bg="silver")
    l_d4.grid(row=6, column=0)

    gen_en = Label(f2_dep, bg="silver", fg="#2c3e50")
    gen_en.grid(row=6, column=1, ipadx=100)

    bl = Label(f2_dep, text="Balance", padx=30, bg="silver")
    bl.grid(row=6, column=2)

    bl_e = Label(f2_dep, bg="silver", fg="#2c3e50")
    bl_e.grid(row=6, column=3, ipadx=100)

    ed_1.configure(width=7)
    ed_2.configure(width=7)
    ed_3.configure(width=7)
    ed_7.configure(width=7)
    ed_5.configure(width=7)
    ed_8.configure(width=7)
    ed_6.configure(width=7)
    act_en.configure(width=7)
    gen_en.configure(width=7)
    bl_e.configure(width=7)

    ask = Label(master, text="Account Number", bg="silver", font="Arial 16")
    ask.place(x=195, y= 170)

    answ = Entry(master, bd=2, relief="groove")
    answ.place(width=200, height=26, x=340, y=169)

    def srch_dep():
        global srch_val
        global all_val

        srch_val = []
        all_val = []
        if answ.get() != "":
            db_dep = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
            cur = db_dep.cursor()

            cur.execute('''SELECT * FROM info''')
            for i in cur.fetchall():
                all_val.append(i[5])

            sql_dep = f'''SELECT * FROM info WHERE Account_No = {answ.get()}'''

            cur.execute(sql_dep)
            srch_val.append(cur.fetchall())

            db_dep.close()

            if int(answ.get()) in all_val:

                ed_1.configure(text=srch_val[0][0][0])
                ed_2.configure(text=srch_val[0][0][1])
                ed_3.configure(text=srch_val[0][0][2])
                ed_7.configure(text=srch_val[0][0][6])
                ed_5.configure(text=srch_val[0][0][4])
                ed_8.configure(text=srch_val[0][0][7])
                ed_6.configure(text=srch_val[0][0][5])
                act_en.configure(text=srch_val[0][0][8])
                gen_en.configure(text=srch_val[0][0][3])
                bl_e.configure(text=srch_val[0][0][9])
            else:
                messagebox.showerror("Error", "Account No Not found!")
                answ.delete(0, END)

        else:
            messagebox.showerror("Error", "Check Account Number!")

    srch_b = Button(master, text="Search", padx=30, command=srch_dep)
    srch_b.place(x=548, y=170)

    #############################################################

    dep_var = StringVar()
    dep_var.set("Cash")

    ac_l2 = Label(f3_dep, text="Deposit Type", bg="silver", font="Arial 13")
    ac_l2.place(x=50, y=30)

    ac_answ = OptionMenu(f3_dep, dep_var, "Cash", "Transfare")
    ac_answ.place(x=140, y=29)

    ac_answ.configure(width=10)

    ac_l3 = Label(f3_dep, text="From Account No", bg="silver", font="Arial 13")
    ac_l3.place(x=400, y=30)

    ac_en3 = Entry(f3_dep, bd=2, relief="groove")
    ac_en3.place(width=200, height=26, x=580, y=29)

    ac_l = Label(f3_dep, text="Amount", bg="silver", font="Arial 16")
    ac_l.place(x=200, y=100)

    ac_en = Entry(f3_dep, bd=2, relief="solid")
    ac_en.place(width=200, height=26, x=290, y=99)

    def dep():
        global old_balance
        global acc_nums
        global email_add
        global f_email
        global formatted_date
        global all_val

        if answ.get() != "" and ac_en.get() != "" and int(ac_en.get()) > 0 and dep_var.get() == "Cash":

            if_cash = messagebox.askyesnocancel("Warning",
                                                f"Are you sure you want to deposit {ac_en.get()} to this account No: {answ.get()}")

            if if_cash == True:
                old_balance = None
                email_add = None
                all_val = None

                # Updating balance in the database
                db = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
                cr = db.cursor()

                acc_sql = f'''SELECT balance FROM info WHERE Account_No = {int(answ.get())}'''
                cr.execute(acc_sql)
                old_balance = cr.fetchall()

                email_sql = f'''SELECT Caste FROM info WHERE Account_No = {int(answ.get())}'''
                cr.execute(email_sql)
                email_add = cr.fetchall()

                sql = f'''UPDATE info SET balance = {int(ac_en.get()) + old_balance[0][0]} WHERE Account_No = {int(answ.get())}'''
                cr.execute(sql)

                all_sql = f'''SELECT * FROM info'''
                cr.execute(all_sql)
                all_val = cr.fetchall()

                db.commit()
                db.close()
                '''
                # refresh customer-treeview
                for child in my_tree2.get_children():
                    my_tree2.delete(child)
                for x in all_val:
                    my_tree2.insert("", "end", values=x)
                #######################################
                '''
                # Transactions page
                tr_db(ac_en.get(), answ.get())
                ######################

                # emailing the customer with details
                #send_email(email_add[0][0], ac_en.get(), answ.get())

                ac_en.delete(0, END)

                messagebox.showinfo("Message", "Success!")
                # customer_list(fram4)


            else:
                ac_en.delete(0, END)
        elif answ.get() != "" and ac_en.get() != "" and int(
                ac_en.get()) > 0 and dep_var.get() == "Transfare" and ac_en3.get() != "":

            if_transfare = messagebox.askyesnocancel("Warning",
                                                     f"Are you sure you want to deposit {ac_en.get()} to this account No: {answ.get()} from this account No: {ac_en3.get()} !")
            if if_transfare == True:

                from_balance = None
                to_balance = None
                f_email = None

                db2 = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
                cr2 = db2.cursor()

                sql_acc_n = f'''SELECT Account_No FROM info'''
                cr2.execute(sql_acc_n)
                acc_nums = cr2.fetchall()

                sql_from = f'''SELECT balance FROM info WHERE Account_No = {int(ac_en3.get())}'''

                cr2.execute(sql_from)
                from_balance = cr2.fetchall()

                if int(ac_en3.get()) in [x[0] for x in acc_nums] and from_balance[0][0] - int(ac_en.get()) > 0:
                    check_sql = f'''UPDATE info SET balance = {from_balance[0][0] - int(ac_en.get())} WHERE Account_No = {int(ac_en3.get())}'''
                    cr2.execute(check_sql)

                    email_sql2 = f'''SELECT Caste FROM info WHERE Account_No = {int(ac_en3.get())}'''
                    cr2.execute(email_sql2)
                    f_email = cr2.fetchall()

                    email_sql = f'''SELECT Caste FROM info WHERE Account_No = {int(answ.get())}'''
                    cr2.execute(email_sql)
                    email_add = cr2.fetchall()

                    sql_to = f'''SELECT balance FROM info WHERE Account_No = {int(answ.get())}'''
                    cr2.execute(sql_to)
                    to_balance = cr2.fetchall()

                    add_sql = f'''UPDATE info SET balance = {to_balance[0][0] + int(ac_en.get())} WHERE Account_No = {int(answ.get())}'''
                    cr2.execute(add_sql)

                    all_sql = f'''SELECT * FROM info'''
                    cr2.execute(all_sql)
                    all_val = cr2.fetchall()

                    db2.commit()
                    db2.close()

                    # Transactions page
                    tr_db_from(ac_en.get(), ac_en3.get(), answ.get())
                    ##################

                    #send_eamil2(f_email[0][0], ac_en.get(), ac_en3.get())
                    #send_email(email_add[0][0], ac_en.get(), answ.get())

                    ac_en.delete(0, END)
                    ac_en3.delete(0, END)

                    '''
                    # refresh customer-treeview
                    for child in my_tree2.get_children():
                        my_tree2.delete(child)
                    for x in all_val:
                        my_tree2.insert("", "end", values=x)
                    #######################################
                    '''
                    messagebox.showinfo("Message", "Succes!")


                else:
                    messagebox.showerror("Error", "Wrong Account No, or Not enogh money!")

            else:
                ac_en.delete(0, END)
                ac_en3.delete(0, END)
        else:
            messagebox.showerror("Error", "Check All required feilds !")

    ac_b = Button(f3_dep, text="Deposit", bg="green", fg="white", padx=30, pady=7, command=dep)
    ac_b.place(x=320, y=150)

    #############################################################

    l = Label(master, text="Usd Prices $", bg="silver", font=("Arial 16"), bd=1, relief="solid")
    l.place(x=975, y=86)

    styl = ttk.Style()
    styl.configure("Custom.Treeview", background="silver", foreground="#17202a", fieldbackground="silver")
    styl.map("Custom.Treeview", background=[("selected", "green")])

    s_b = Scrollbar(f1_dep)
    s_b.place(height=300, x=226, y=0)
    exch_tree = ttk.Treeview(f1_dep, yscrollcommand=s_b.set, style="Custom.Treeview")

    exch_tree["columns"] = ["Name", "Price"]
    exch_tree["show"] = "headings"

    exch_tree.heading("Name", text="Name")
    exch_tree.heading("Price", text="Price")

    exch_tree.column("Name", width=100)
    exch_tree.column("Price", width=98)

    def usd_pr():

        try:
            # requesting and parsing web page to get usd exchange
            req = requests.get("https://www.exchangerates.org.uk/US-Dollar-USD-currency-table.html")
        except:
            messagebox.showerror("Error", "Check Connection!!!")

        else:

            soup = bs(req.text, "lxml")

            # putting the data into pandas Dataframe as table
            df = pd.read_html(str(soup.find_all(class_="currencypage-mini")[1]))[0]
            # filtring the Dataframe
            df.dropna(axis="columns", how="all", inplace=True)
            for child in exch_tree.get_children():
                exch_tree.delete(child)

            for x in df.values.tolist():
                exch_tree.insert("", "end", values=x[0:2])

    usd_b = Button(master, text="Get prices", bg="silver", padx=30, command=usd_pr)
    usd_b.place(x=980, y=440)

    exch_tree.place(width=225, height=300, x=0, y=0)
    s_b.config(command=exch_tree.yview)

