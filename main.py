import pandas
import datetime
import random
import smtplib
##################### Extra Hard Starting Project ######################

EMAIL = "your_email_here"
SECURE_PASSWORD = "your_provider_password_here"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dic = {(data_row["month"], data_row["day"])
                  : data_row for (index, data_row) in data.iterrows()}
today = datetime.datetime.now()
today_tuple = (today.month, today.day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dic:
    random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dic[today_tuple]
    with open(random_letter) as letter:
        letter_text = letter.read()
        letter_text = letter_text.replace("[NAME]", birthday_person["name"])


# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=SECURE_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:HAPPY BIRTHDAY\n\n{letter_text}"
        )
