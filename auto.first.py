#Section 1
# Intro to web scraping.
#Setting up a env.
#project architecture
#Building a scraper
#Sending emals

#------------------------------------------#
#      Project Architecture overview       #
#------------------------------------------#
# Request Module: HTTP requests, get.
# BeautifulSoup4: Web Scraping.
# SMTPlib: emal auth and transaction
# email.mine: to create email body
# datetime: access time

import requests #http requests
from bs4 import BeautifulSoup # web scraping
import smtplib # email, auth and transtaction
#Email Body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = "" #email content placeholder.

def extract_news(url):
    print("Extraction Hacker News Stories...")
    cnt = ''
    cnt += ('<b>HN Top Stories:<b>\n'+'<br>'+'-'*20+'<br>')
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    for i, tag in enumerate(soup.find_all('td', attrs={"class":"title"})):
        cnt +=((str(i+1)+ ' :: '+ tag.text + "\n"
                + '<br>') if tag.text!='More' else '')
        
        #print (tag.prettify) #finall('span', atrs= {'class' : 'sitestr'})
    
    return cnt

content += extract_news('https://news.ycombinator.com/')
content += ("<br>--------------------<br>")
content += ('<br><br>End of Message')

#Sending an Email.
# print(content)

print("composing Email...")
# Update your email details.
SERVER = "smtp.gmail.com" #your smtp server
PORT = 587 #Your port number.


from pathlib import Path
from dotenv import load_dotenv
import os

env_file = Path(__file__).parent / ".env"
load_dotenv(env_file)

FROM = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_PASS")


#PREM- mypccyberzone@gmail.com
#ARYAN = aryankaushal269@gmail.com
#NITIN = nk8126852@gmail.com
#SUMIT = sumitkumarsk2929@gmail.com
TO = "sumitkumarsk2929@gmail.com" # your email id
msg = MIMEMultipart()

msg['Subject'] = "Top news Stories HN [Automated]" + " " + str(now.day) + '-' + str(now.month) + "-" + str(now.year)

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))


print("Initiating Server...")

server = smtplib.SMTP(SERVER, PORT)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
