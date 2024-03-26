import smtplib
import random
import datetime as dt


now = dt.datetime.now()
weekday = now.weekday()

my_email = "animezon.stha@gmail.com"
password = "mero nznt nyva ecfm"


if weekday == 1:
    with open("Birthday Wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs = my_email, 
                msg = f"Subject:Quote of the day\n\n{quote}"
            )