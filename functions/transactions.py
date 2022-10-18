from tkinter import *
from tkinter import ttk
from mysql import connector
import datetime



def tr_db(amount,account_no):
    # Transactions page
    db_tr = connector.connect(host = "localhost",user = "root",passwd = "password",database = "bank_db")
    cr_tr = db_tr.cursor()

    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')


    tr_sql = tr_sql = f'''INSERT INTO transactions (date,employee_id,transaction) VALUES (%s,%s,%s)'''
    in_val = (formatted_date,0,f"a {amount} lyd has been deposit to this account No {account_no} in cash.")

    cr_tr.execute(tr_sql,in_val)
    db_tr.commit()
    db_tr.close()
    ######################

def tr_db_from(amount,account_no,account_no2):
    # Transactions page
    db_tr = connector.connect(host = "localhost",user = "root",passwd = "password",database = "bank_db")
    cr_tr = db_tr.cursor()

    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')


    tr_sql = tr_sql = f'''INSERT INTO transactions (date,employee_id,transaction) VALUES (%s,%s,%s)'''
    in_val = (formatted_date,0,f"a {amount} lyd has been transfared from this account No {account_no} to this account No {account_no2} .")

    cr_tr.execute(tr_sql,in_val)
    db_tr.commit()
    db_tr.close()
    ######################

def transactions():
    global tr_val

    page = Toplevel()
    page.geometry("900x600+280+90")
    page.config(bg="silver")

    tr_title = Label(page, text="Transactions Page", padx=30, font="Arial 23", bd=2, relief="raised")
    tr_title.place(x=300, y=10)

    sty = ttk.Style()
    sty.theme_use("alt")
    sty.configure("custom2.Treeview", background="silver", feildbackground="silver")
    sty.map("custom2.Treeview", background=[("selected", "green")])

    tree = ttk.Treeview(page, style="custom2.Treeview")
    tree["columns"] = ["Date", "Employee_id", "Transaction"]
    tree["show"] = "headings"

    for x in ["Date", "Employee_id", "Transaction"]:
        tree.heading(x, text=x)

    tree.column("Date", width=150)
    tree.column("Employee_id", width=100)
    tree.column("Transaction", width=625)

    db_tr2 = connector.connect(host="localhost", user="root", passwd="password", database="bank_db")
    cr_tr2 = db_tr2.cursor()

    tr_sql2 = f'''SELECT * FROM transactions'''

    cr_tr2.execute(tr_sql2)
    tr_val = cr_tr2.fetchall()

    db_tr2.commit()
    db_tr2.close()

    for v in tr_val:
        tree.insert("", "end", values=v)

    tree.place(width=880, height=500, x=10, y=90)

    def pop_up(s):
        global selected_v

        pop = Toplevel()
        pop.geometry("500x300+400+200")

        selected = tree.focus()
        selected_v = tree.item(selected, "values")

        tex = Text(pop, width=500, height=400, bg="silver")
        tex.pack()

        show = f"in {selected_v[0].split()[0]} at {selected_v[0].split()[1]} the employee with this Id {selected_v[1]} \n\ndid this : {selected_v[2]}"
        tex.insert(END, show)

        mainloop()

    tree.bind("<Double-1>", pop_up)

    mainloop()