import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com.br/Sony-Mirrorless-24-105mm-Filtro-Cart%C3%A3o/dp/B00VAWBA8I/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1586371998&s=electronics&sr=1-5'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'} # define my user agent

def check_price():
    page = requests.get(URL, headers=header) #get the page inserting URL and User Agent

    soup = BeautifulSoup(page.content, 'html.parser') #turn into an html file

    title = soup.find(id='productTitle').get_text() #get the text of the title of the product

    print(title.strip())

    price = soup.find(id='priceblock_saleprice').get_text() #get the price of the product
    converted_price = float(price[2:8]) #extract only numbers in price and turn parse into a float

    if (converted_price > 15):
        send_mail()

    print(converted_price)

def send_mail():
    sender_email = 'matheus.abrao99@gmail.com'
    receiver_email = 'mabrao99@outlook.com'
    password = 'tgrgosndhvifcrou'
    #password = input(str('Please enter your password: '))
    body = 'Python detected a fall on the price of the product! CHeck the link: https://www.amazon.com.br/Sony-Mirrorless-24-105mm-Filtro-Cart%C3%A3o/dp/B00VAWBA8I/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1586371998&s=electronics&sr=1-5'
    subject = 'Price fell down!'

    message = f'Subject: {subject}\n\n{body}'
    server = smtplib.SMTP('smtp.gmail.com', 587) #create a server
    server.ehlo() #establishes connection betweeen two emails
    server.starttls() #encrypts connection
    server.ehlo() #establishes connection betweeen two emails
    server.login(sender_email, password)
    print('Login successful')
    server.sendmail(sender_email, receiver_email, message)
    print('Email has been sent to ', receiver_email)
    server.quit()

check_price()