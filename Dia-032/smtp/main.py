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
from dotenv import load_dotenv
import os

import datetime as dt
import smtplib
import random
load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
now = dt.datetime.now()
weekday = now.weekday()

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