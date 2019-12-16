from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

name = input('Name of the group or user to fuck: ')
message = input('mESSAGE to fuck '+name+": ")
count = int(input('Number of messsages: '))

input('Enter enything alter scanning the qr code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_3u328.copyable-text.selectable-text")
try:
    for i in range(count):
        msg_box.send_keys(message+Keys.ENTER)
except:
    print("Failure in fucking "+name)
finally:
    print(name+" fucked sucessfully!")