from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# Nicolas Alicia Maldonado Florencia 
#URL = "https://example.com/yourdataurl.php"
#'''
#Data json example
#[{'id': '12', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': 'xxxxxxxxxx', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '11', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': 'xxxxxxxxxx', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '10', '_user_id': '11', '_from': 'xxxxxxxxxx', '_to': '8126458906', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MDRhNWEwZjZkOA==', 'is_sent': '0'},
#    {'id': '13', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': '9717746592', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '14', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': '9555061457', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '15', '_user_id': '11', '_from': 'xxxxxxxxxx', '_to': '9990377643', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MDRhNWEwZjZkOA==', 'is_sent': '0'}]
#You can change data format as you want
#'''
#PARAMS = {}
#r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
# data = r.json()
# input number from which you want to send whatsapp message
# phone = input("phone: ")
phone = "9 11-6223-5902"
client = requests.Session()
# client.headers.update({'Connection': 'Keep-Alive'})
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# Change user-data-dir path with your local path, where you want to save session
chrome_options.add_argument(
    f"user-data-dir=C:\\Usuarios\\PC\\AppData\\Local\\Google\\Chrome\\User Data\\+54{phone}")

# Change chrome driver path driver = webdriver.Chrome(r'C:\chromeDriver\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome('C:\\Users\\PC\\Desktop\\whatsapp-automation-master\\driver\\chromedriver.exe',
                          chrome_options=chrome_options)
#count = 0
#data = [
#    {"_to": "Mateo", "_message": "hello"},
#    {"_to": "Leslie", "_message": "helloo"}, 
#]
driver.get("https://web.whatsapp.com/")

name = input('enter the name of user:')
msg = input('enter your message:')
#count = int(input("enter the count:"))
input('enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]') #/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]
time.sleep(3)

#for i in range(count):
msg_box.send_keys(msg)
time.sleep(10)
button = driver.find_element_by_class_name('_4sWnG')
button.click()
print("Mensaje enviado!")


#for i in data:
#    time.sleep(2)
#    wait = WebDriverWait(driver, 600)
#
#    try:
#        alert = driver.switch_to.alert
#        alert.accept()
#    except:
#        pass
#
#    try: 
#        find_contact= driver.find_element_by_class_name("_1Jn3C")
#        #find_contact= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_1Jn3C")))
#        find_contact.click()
#        time.sleep(20)
#        print("Caja de busqueda encontrada.")
#    except:
#      pass
#
#    try:
#        type_contact=driver.find_element_by_class_name("_1Jn3C")
#        #type_contact = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_3Qnsr")))
#        type_contact.send_keys(i["_to"])
#        print("Usuario escrito.")
#        time.sleep(15)
#    except:
#        pass
#
#    try:
#        select_contact= driver.find_element_by_class_name("_3OvU8")
#        select_contact.click()
#        time.sleep(20)
#        print("Usuario click.")
#    except:
#        pass
#
#    try:
#        group_title= driver.find_element_by_class_name("p3_M1") #p3_M1
#        group_title.click()
#        #group_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_1Plpp")))
#        group_title.send_keys(i["_message"])
#        print("Caja de texto encontrada.")
#        time.sleep(10)
#    except Exception as e:
#        print(e)
#        pass
#
#    try:
#        group_titles= driver.find_element_by_class_name("_4sWnG")
#        #group_titles = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_35EW6")))
#        group_titles.click()
#        print("Mensaje enviado.")
#    except Exception as e:
#        print(e)
#        pass

driver.close()
