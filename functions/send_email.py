import smtplib
from email.message import EmailMessage



def send_email(email, value, account_no):
    msg = EmailMessage()
    msg["subject"] = "Transfare Money"
    msg["from"] = "your email"
    msg["to"] = [email]
    msg.set_content(f"\t\t------- a {value} Lyd ----------\nhas been deposed to this bank account number: {account_no}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.login("your email", "your third party app pass")
        conn.send_message(msg)


def send_eamil2(email, value, account_no):
    msg2 = EmailMessage()
    msg2["subject"] = "Transfare Money"
    msg2["from"] = "your email"
    msg2["to"] = [email]
    msg2.set_content(
        f"\t\t------- a {value} Lyd ----------\nhas been cutted from this bank account number: {account_no}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.login("your email", "your third party app pass")
        conn.send_message(msg2)
