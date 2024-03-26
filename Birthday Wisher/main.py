import smtplib

my_email = "animezon.stha@gmail.com"
password = "mero nznt nyva ecfm"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr = my_email, 
        to_addrs = my_email, 
        msg = "Subject:Hello\n\nThis it the body of the email."
    )