import random
import smtplib
import pandas
import datetime as dt
import os


data = pandas.read_csv("birthdays.csv")
month_list = data["month"].to_list()
day_list = data["day"].to_list()


now = dt.datetime.now()
month = now.month
day = now.day
chosen_row = data[data.day == day]

directory = "./letter_templates"
letter_list = os.listdir(directory)
template_file = random.choice(letter_list)


with open(f"./letter_templates/{template_file}", "r") as temp:
    content = temp.read()
    for index, row in chosen_row.iterrows():
        letter = content.replace("[NAME]", str(row["name"]))

if month in month_list and day in day_list:
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        my_email = "48.xiib.muskanjaggi@gmail.com"
        password = "vltr bjdv wnnr cvcf"
        con.login(user=my_email, password=password)

        con.sendmail(from_addr=my_email, to_addrs= chosen_row["email"],
                     msg=f"Subject: HAPPY BIRTHDAY!\n\n {letter}")


