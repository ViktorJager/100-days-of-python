import smtplib
import datetime as dt
import random

MONDAY = 6

# Burner mail for testing
my_email = "groteskovilja@gmail.com"
pw = "groteskovilja123"
to_addr = "mjonsson900@gmail.com"


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=to_addr, msg=message)


message = "Subject:Big opportunity for money making!\n\nHello, my name is GO\nI have money making opportunity. Please contact me for more or less information.\nKoromass."


with open("quotes.txt", "r") as file:
    quotes = file.readlines()

quote = random.choice(quotes)
mail_msg = "Subject:Motivational quote of the day\n\n" + quote

now = dt.datetime.now()
day = now.weekday()

if day == MONDAY:
    for _ in range(10):
        send_mail(mail_msg)
