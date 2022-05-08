import smtplib
import datetime as dt
import random
import pandas as pd


# Burner mail for testing
my_email = "groteskovilja@gmail.com"
pw = "groteskovilja123"
to_addr = "mjonsson900@gmail.com"

birthday_list = pd.read_csv("birthdays.csv").to_dict(orient="index")


def send_birthday_mail(name):
    # Generate personalized birthday wish
    birthday_mail = generate_birtday_mail(name)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=to_addr, msg=birthday_mail)


def generate_birtday_mail(name):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        random_letter = letter.readlines()
        birthday_wish = random_letter[0].replace("[NAME]", name.title())
        for line in random_letter[1:]:
            birthday_wish += line

    email_subject = f"Subject:Happy birthday {name.title()}!\n\n"

    return email_subject + birthday_wish


now = dt.datetime.now()
todays_month = now.month
todays_day = now.day

for human in birthday_list.values():
    name = human["name"]
    birthday_month = human["month"]
    birthday_day = human["day"]

    if birthday_month is todays_month and birthday_day is todays_day:
        send_birthday_mail(name)
