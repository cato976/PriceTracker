import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amd.com/en/support/chipsets/amd-socket-am4/x570'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_availability():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #print(soup.prettify())
    
    name = soup.find(attrs={"field--name-name"}).get_text()
    price = soup.find(attrs={"field--name-revision-number"}).get_text()
    print(name.strip())
    print(price.strip())
    #print("Is it out of stock")
    if(price.find("2.04.04.111")):
        print('still at 2.04.04.111')
    else:
        send_mail()
    #print(name.strip())
    #print(price.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    subject = "Chipset available!"
    boby = "AMD chipset changed" + URL

    msg = f"Subject: {subject}\n\n{boby}"

    server.sendmail('andrecato@gmail.com', 'andrecato@gmail.com',msg)
    print('EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_availability()
    time.sleep(60 * 60 * 24)
