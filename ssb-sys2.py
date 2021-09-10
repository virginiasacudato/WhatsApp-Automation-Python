
from bs4 import BeautifulSoup
import requests
#import cookielib ## http.cookiejar in python3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")
USER = os.environ.get("USER")
PASSWORD_USER = os.environ.get("PASSWORD_USER")

#cj = cookielib.CookieJar()
#br = mechanize.Browser()
#br.set_cookiejar(cj)
#br.open(URL)

url = "https://app.ssbint.com/SSB/LogIn.aspx?ReturnUrl=/SSB/default.aspx"
myobj = {"hidden_user":USER, "hidden_password":PASSWORD_USER}
with requests.session() as session:
  response = session.post(url, data=myobj)
  print(response.text)


#br.select_form(nr=0)
#br.form['userinput'] = USER
#br.form['passwordinput'] = PASSWORD_USER
#br.submit()

#print br.response().read()