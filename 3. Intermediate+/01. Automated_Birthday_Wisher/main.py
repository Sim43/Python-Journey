import pandas as pd 
import smtplib
import random
import datetime as dt

def send_letter(name, reciever_email):
    random_sno = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_sno}.txt", "r") as file:
        filedata = file.read()
    filedata = filedata.replace("[NAME]", name)
    filedata = filedata.replace("Angela", "Zero")
    
    sender_email = "youremail@gmail.com"
    sender_password = "abcd"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email, to_addrs=reciever_email, msg=f"Subject: Happy Birthday\n\n{filedata}")



now = dt.datetime.now()
day = now.day
month = now.month

df = pd.read_csv("birthdays.csv")
target = df[df.month == month]
try:
    name = target.name.iloc[0]
    reciever_email = target.email.iloc[0]
    send_letter(name, reciever_email)
except IndexError:
    pass
    




