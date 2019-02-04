import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
email = "luisthemaster3@gmail.com"
password = "H1cc$43*"
palabras=[
"abad"]
import sqlite3
conn = sqlite3.connect('seccion.db')
c = conn.cursor()
#leer bien----	
"""c.execute('''DROP TABLE acceso''')

#c.execute('''CREATE TABLE acceso
            (id integer auto_increment primary key, email text, password text)''')
#Insert a row of data
c.execute("INSERT INTO acceso VALUES (1,'luisthemaster3@gmail.com','H1cc$43*')")
conn.commit()
#Save (commit) the changes
c.execute("INSERT INTO acceso VALUES (2,'ccidbcomputacion12@gmail.com','H1cc$43*')")
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#c.execute("SELECT * FROM acceso")
#print (c.fetchone))
"""
seccion=dict()
for row in c.execute('SELECT * FROM acceso'):seccion.update({row[0]:{'users':row[1],'password':row[2]}})
#row[0]=id, row[1]=usuario row[2]=password
#print(seccion)
#print(seccion[1]['users'])
#print(seccion[1]['password'])
conn.close()
    #binary = FirefoxBinary('/usr/bin/firefox')
    #driver = webdriver.Firefox(firefox_binary=binary)
    #abrir navegador
def main():
    driver = webdriver.Chrome()
    driver.get("https://www.presearch.org/login")
    print("iniciandoooooooooooo")
    def buscar():
        cantidad= (len(palabras))
        for x in range(0, cantidad):
            t.sleep(2)
            cb = driver.find_element_by_name("term")
            cb.send_keys(palabras[x])
            t.sleep(2)
            bn = driver.find_element_by_css_selector("button.rounded").click()
            driver.back()
            driver.refresh()
            t.sleep(2)            
    for x in seccion:
        username_field = driver.find_element_by_name("email")
        password_field = driver.find_element_by_name("password")
        login_button = driver.find_element_by_css_selector('button.btn-primary')        
        #print(seccion[x]['users'],(seccion[x]['password']))
        elem = driver.find_elements_by_class_name("tour-balance")         
        for banlance in elem:print (seccion[x]['users']+banlance.text)
        username_field.send_keys(seccion[x]['users'])
        t.sleep(2)
        password_field.send_keys(seccion[x]['password'])
        t.sleep(2)
        login_button.click()
        buscar()
        driver.close()
        t.sleep(2)
        driver = webdriver.Chrome()
        driver.get("https://www.presearch.org/login")   
main()
