from datetime import datetime
import smtplib
import pandas
import random

today = datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "animezon.stha@gmail.com"
MY_PWD = "mero nznt nyva ecfm"

birthday_csv = "Birthday Wisher/birthdays.csv"

data = pandas.read_csv(birthday_csv)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PWD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=birthday_person["email"], 
                msg=f"Subject: Happy Birthday {birthday_person["name"]}!\n\n{content}"
            )