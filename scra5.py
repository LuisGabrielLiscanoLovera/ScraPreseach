#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
import sqlite3
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display
print("*****--------------Thanks for play XD--------------*****\n")
conn = sqlite3.connect('seccion.db')
c = conn.cursor()
""" c.execute('''DROP TABLE acceso''')
c.execute('''CREATE TABLE acceso (id integer auto_increment primary key, email text, password text)''')
c.execute("INSERT INTO acceso VALUES (1,'luisthemaster3@gmail.com','H1cc$43*')")
conn.commit()
c.execute("INSERT INTO acceso VALUES (2,'ccidbcomputacion12@gmail.com','H1cc$43*')")
conn.commit()
 """
seccion=dict()
for row in c.execute('SELECT * FROM acceso'):seccion.update({row[0]:{'users':row[1],'password':row[2]}})
conn.close()
palabras =[	"php",	"python",	"larvel",	"crane",	"vue",	"vuetify",	"java",	"devOps",	"jenkins",	"javascript",	"ccs",	"sass",	"software",	"develoment",	"codificacion",	"integracion",	"pruebas Unitarias",	"Despliege",	"fomentar la cultura de programacion agil",	"integracion continua",	"kotlin",	"android",	"red",	"try",	"css",	"sass",	"webpack",	"refactorize",	"replase",	"inner join",	"sql manager",	"capitalize",	"station"]

def main():
	try:
		options = Options()#<--------------------Hiden Browser
		options.add_argument("--headless")
		driver = webdriver.Firefox(options=options,executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox')
		driver.get("https://www.presearch.org/login");
		cantidad = (len(palabras))
		def buscar():
			for x in range(0, cantidad):
				cb = driver.find_element_by_name("term");cb.send_keys(palabras[x]);t.sleep(2);bn = driver.find_element_by_css_selector("button.rounded").click();driver.back();driver.refresh();t.sleep(2)
		
		for x in seccion:
			username_field = driver.find_element_by_name("email");password_field = driver.find_element_by_name("password")
			login_button = driver.find_element_by_css_selector('button.btn-primary')
			username_field.send_keys(seccion[x]['users']);t.sleep(2)
			password_field.send_keys(seccion[x]['password']);t.sleep(3)
			login_button.click();t.sleep(3)
			elem = driver.find_elements_by_class_name("tour-balance")         
			
			for inicioBalance in elem:print("-----------------------\n"+str(x)+")Usuario: ["+seccion[x]['users']+"] Acomulado: {"+(inicioBalance.text)+"}")	
			buscar()
			elemD = driver.find_elements_by_class_name("tour-balance")         
 			
			for finalBalance in elemD:
				f = finalBalance.text
				final=1000.00-(float(f.replace("PRE", "", 3)))
				print("Final obtenido: {"+(finalBalance.text)+"}")
				print("Total tokens Faltante: {"+str(final)+"}")
			driver.close();driver = webdriver.Firefox(options=options,executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox');driver.get("https://www.presearch.org/login")
		
		driver.close()
		
	except Exception as e: print(e)
if __name__ == '__main__':
	main()
#descaomentar para mostrar el contenido de la paguina 
#html = driver.page_source