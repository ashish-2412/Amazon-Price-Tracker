import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL= input("Enter the URL of the Amazon Product : ")
price_wanted=int(input("Enter the price you want : "))
user_agent = input("Enter your Browser's User-Agent : (Search ""My User Agent"" on www.google.com)")
headers={'User-Agent':user_agent}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text().strip()
    price=int(soup.find(id="priceblock_ourprice").get_text()[1:5].strip())
    print(title)
    print(price)
    if price<price_wanted:
        send_mail()

def send_mail():
    sender_email=input("Enter the sender's email address : ")
    sender_password=input("Enter the sender's password : ")
    reciever_email=input("Enter the reciever's email address : ")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email,sender_password)
    subject="Price fell down!"
    body='Check the amazon link : '+URL
    msg=f"Subject : {subject} \n\n {body}"
    server.sendmail(
        sender_email,
        reciever_email,
        msg
    )
    print("Email sent")
    server.quit() 

check_price()