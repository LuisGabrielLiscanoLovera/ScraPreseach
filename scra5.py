#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#import sqlite3
#conn = sqlite3.connect('seccion.db')
palabras=[
"php",
"python",
"django",
"flask"]
'''
"larvel",
"crane",
"vue",
"vuetify",
"java",
"devOps",
"jenkins",
"javascript",
"ccs",
"sass",
"software",
"develoment",
"codificacion",
"integracion",
"pruebas Unitarias",
"Despliege",
"fomentar la cultura de programacion agil",
"integracion continua",
"kotlin",
"android",
]
'''
email ="luisthemaster3@gmail.com"
password = "H1cc$43*"

def main():	
	try:
		#inicia la configuracion del navegador
		driver = webdriver.Firefox(
			executable_path='/usr/local/bin/geckodriver',
    		firefox_binary='/usr/bin/firefox')
		driver.get("https://www.presearch.org/login")
		
		
		
		#login-in Inici seccion	
		
		t.sleep(3)
		username_field = driver.find_element_by_name("email")
		password_field = driver.find_element_by_name("password")
		login_button = driver.find_element_by_css_selector('button.btn-primary')		
		

		username_field.send_keys(email)
		password_field.send_keys(password)
		login_button.click()
		
		
		
		
		
		
		
		#espera 3 segundo y luego regresa		
		def showBalance():
			t.sleep(2)
			elem = driver.find_elements_by_class_name("tour-balance")
			for banlance in elem:
				print (driver.title +"\nUsuario: " +email+ "\nBalance: "+ banlance.text)
		print("primer Balance antes de iniciar la app")
		showBalance()
	 	#Inicio de la Busqueda 
		
		def busqueda():
			for palabra in palabras:
				t.sleep(2)
				search = driver.find_element_by_name('term').send_keys(palabra)
				driver.find_element_by_css_selector('button.rounded').click()
				t.sleep(5)
				driver.back()
				driver.refresh()
			showBalance()
		
		busqueda()
		

		#Muestra los balances		
		#print("final Balance depues de terminar la seccion")
		#gorefresh(driver)
		#showBalance()

 	except Exception as e: print(e)
if __name__ == '__main__':
	main()
#descaomentar para mostrar el contenido de la paguina 
#html = driver.page_source





