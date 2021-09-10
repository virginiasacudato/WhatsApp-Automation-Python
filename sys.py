# pip install -r requirements.txt
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import math 
import re

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import os
from os.path import join, dirname
from dotenv import load_dotenv

from datetime import date, datetime
from os import walk, path

fecha = date.today()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")
USER = os.environ.get("USER")
PASSWORD_USER = os.environ.get("PASSWORD_USER")

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome('C:\\Users\\PC\\Desktop\\whatsapp-automation-master\\driver\\chromedriver.exe',
                          options=chrome_options)

action = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(URL)

login = driver.find_element_by_xpath(
                        '//*[@id="userinput"]')
login.send_keys(USER)
print("Usuario escrito.")
time.sleep(2)


login_password = driver.find_element_by_xpath(
                        '//*[@id="passwordinput"]')
login_password.send_keys(PASSWORD_USER)
print("Contraseña escrita.")
time.sleep(2)

button = driver.find_element_by_xpath(
                        '//*[@id="acceptbutton"]')
button.click()
print("Sesion iniciada.")
time.sleep(2)

button_admin = driver.find_element_by_xpath(
                        '//*[@id="FrameworkMenu"]/ul/li[3]/a')
button_admin.click()
print("Boton de Pedidos")
time.sleep(2)

button_admin_pedidos = driver.find_element_by_xpath(
                                '//*[@id="FrameworkMenu"]/ul/li[3]/ul/li[2]/a')

button_admin_pedidos.click()
print("Boton de Administracion de pedidos")
time.sleep(7)



#element = driver.find_element_by_xpath("/html/body/div[1]/div/div/table/tbody/tr[2]/td/span/span/div/div/div[3]/div[3]/div/table/tbody/tr[2]/td[2]")
#element.click()
#print("Elemento click")
driver.switch_to.frame("content-iframe")
element2 = driver.find_element_by_class_name('ui-paging-info')

array_elemento = element2.text.split(" ")
total_pedidos = array_elemento[len(array_elemento) - 1]

select_element = driver.find_element(By.CLASS_NAME,'ui-pg-selbox')
select_object = Select(select_element)
pedidos_pag = 20
select_object.select_by_value(str(pedidos_pag))

total_pag = math.ceil(int(total_pedidos.replace(".", ""))/pedidos_pag)
#total_pag = 1




lista_de_pedidos = []
cont_total_pag = 1

while cont_total_pag <= total_pag:
    
   
    cont_pedidos = 1
    while cont_pedidos <= pedidos_pag:
        time.sleep(5)
        
        try:
            print('#ConsultaPedido_grid_grilla > tbody:nth-child(1) tr[id="{}"] td:nth-child(1)'.format(cont_pedidos))
            element_tr = driver.find_element_by_css_selector('#ConsultaPedido_grid_grilla > tbody:nth-child(1) tr[id="{}"] td:nth-child(1)'.format(cont_pedidos))
            #print("Existo :)")
            pedido_id = element_tr.text

            driver.execute_script("window.scrollBy(0, arguments[0]);", 1000)
            element_tr.click()
            detail = driver.find_element_by_xpath('//*[@id="ConsultaPedido_Detalle_BUTTON"]/span')
            detail.click()
            #time.sleep(3)
            elemento_vencimiento_simi = driver.find_element_by_id('ConsultaPedido_detalle_SolapaDatos_VtoSIMI_TEXTBOX') #ConsultaPedido_detalle_SolapaDatos_VtoSIMI_TEXTBOX
            vencimiento_simi = elemento_vencimiento_simi.get_attribute("value") or "01/01/1999"

            lista_de_pedidos.append(pedido_id+" "+datetime.strptime(vencimiento_simi, "%d/%m/%Y").strftime("%Y-%m-%d"))

            #time.sleep(1)
            driver.back()
            time.sleep(5)
            driver.switch_to.frame("content-iframe")
            next_page_element = driver.find_element_by_class_name('ui-pg-input')

            if cont_pedidos != pedidos_pag:

                #time.sleep(1)
                next_page_element.send_keys(Keys.CONTROL, "a")
                next_page_element.send_keys(cont_total_pag)
                print("Enter "+ str(cont_total_pag))
                #time.sleep(1)
                next_page_element.send_keys(Keys.ENTER)
            cont_pedidos+=1
        except NoSuchElementException:
            print("No existo")
            break

    
    cont_total_pag+=1
    next_page_element = driver.find_element_by_class_name('ui-pg-input')
    
    

    #time.sleep(1)
    next_page_element.send_keys(Keys.CONTROL, "a")
    next_page_element.send_keys(cont_total_pag)
    next_page_element.send_keys(Keys.ENTER)
    #time.sleep(1)
        
        
        #time.sleep(5)
    
    #driver.switch_to.default_content()
    #next_page_element.click()
    time.sleep(3)
print(lista_de_pedidos)
for (dirpath, dirnames, filenames) in walk("listas_simi"):
    if len(filenames) > 0:
        for f in filenames:
            fichero = open(path.join(dirpath, f)).read().split("\n")
            data_to_file = []
            not_in_file = list(np.setdiff1d(lista_de_pedidos,fichero))
            for patata in not_in_file:
                if len(patata.split(" ")) > 1:
                    data_to_file.append(patata.split(" ")[0]+" "+patata.split(" ")[1]+"\n")

                else:
                    data_to_file.append(patata.split(" ")[0]+" "+"\n")
            fichero= open(path.join(dirpath, "lista_simi_{}.txt".format(fecha)), "a")
            fichero.writelines(data_to_file)
    else:
        fichero= open(path.join(dirpath, "lista_simi_{}.txt".format(fecha)), "a")
        fichero.writelines(f'{s}\n' for s in lista_de_pedidos)

os.system("node ./whats-bot-node/index.js")

'''
for (dirpath, dirnames, filenames) in walk("listas_simi"):
    #f.extend(filenames)
    if len(filenames) > 0:

        for f in filenames:
            fichero = open(path.join(dirpath, f))
            data_to_file = ""
            for line in fichero:
                
                id_simi = line.split(" ")[0]
                if not line in lista_de_pedidos:
                    id = line.split(" ")[0]
                    if len(line.split(" ")) > 1:
                        data_to_file = id+" "+line.split(" ")[1]+"\n"
                        print("Manzana"+id_simi)
                    else:
                        data_to_file = id+" "+" "+"\n"
            with open("listas_simi/lista_simi_{}.txt".format(fecha), "a") as text_file:
                text_file.write(data_to_file)
                text_file.close()           
    else: 
        fichero= open(path.join(dirpath, "lista_simi_{}.txt".format(fecha)), "a")
        fichero.writelines(f'{s}\n' for s in lista_de_pedidos)
'''





    
    
        










#click_first =driver.find_element_by_xpath(
#                                  '//*[@id="jqgh_ConsultaPedido_grid_grilla_orden"]/span/span[2]')
#click_first.click()
#print("Elemento click")




#wait = WebDriverWait(driver, 10)
#element = wait.until(driver.find_elements_by_tag_name["td"])
#
#for value in element:
#        print(value.text)
#
#time.sleep(1)

#button_details = driver.find_element_by_xpath(
#                                '//*[@id="ConsultaPedido_Detalle_BUTTON"]')
#button_details.click()
#print("Detalle del pedido.")
#time.sleep(2)





                            
