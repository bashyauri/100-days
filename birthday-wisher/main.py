import smtplib
import datetime as dt
import os
from random import *
import pandas as pd

my_email = "basharumartech@gmail.com"
password = "uzwofkucrrmkackb"
path = os.getcwd()


def send_email(birthday_message, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{email}", msg=f"Subject:Birthday Wishes\n\n{birthday_message}")
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(year)
# print(day_of_week)
# print(date_of_birth)


def pick_letter():
    numbers = [1, 2, 3]
    letter_number = choice(numbers)
    try:
        with open(os.path.join(path, "birthday-wisher/letter_templates", f"letter_{letter_number}.txt"), 'r') as f:
            words = f.readlines()
    except FileNotFoundError:
        print("File not found")
    else:
        return words

try:
    df = pd.read_csv(os.path.join(path, "birthday-wisher", "birthdays.csv"))
except FileNotFoundError:
    print("File not found")
now = dt.datetime.now()
day = now.day
month = now.month

birthday_friends = df[(df['day'] == day) & (df['month'] == month)]
birthday_dict = birthday_friends.to_dict()


for num in range(len(birthday_dict['name'])):

    letter = ''.join(pick_letter())
    email = str(birthday_dict['email'][num])
    name = str(birthday_dict['name'][num])
    birthday_message = letter.replace(
        '[NAME]', name)

    send_email(birthday_message, email)
