# import smtplib
#
# my_email = "udemytest1212@gmail.com"
# password = "zmrq qhmw njqz jckj"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password = password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "udemytest1212@gmail.com"
password = "lmwo qoih mmeq vdkf"

if weekday == 2:
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
        week_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Quote of the day!\n\n{week_quote}".encode("utf-8")
        )