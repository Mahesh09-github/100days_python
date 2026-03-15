birthdays_dict = {}

from datetime import datetime
import pandas as pd
import random
import smtplib
today = datetime.now()
today_tuple = (today.month,today.day)
my_email = "iamjunior009@gmail.com"
password = "ejmr yeos cpph yarb"

data = pd.read_csv("birthday-wisher/birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"birthday-wisher/letter_templates/letter_{random.randint(1,4)}.txt"
    with open(file_path) as file:
        lines = file.read()
        content = lines.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= birthday_person["email"],
                            msg=f"Subjrct:Happy Birthday!\n\n{content}")
else:
    print("Today there isn't anyone's birthday")