#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
import sqlite3
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from numpy  import asarray as np
from random import randint as rd
from json import load as js


print("*****--------------Thanks for play XD--------------*****\n")
conn = sqlite3.connect('seccion.db')
c = conn.cursor()


##############################################Se cargan los usuarios #####################################
#c.execute('''DROP TABLE acceso''')
#c.execute('''CREATE TABLE acceso (id integer auto_increment primary key, email text, password text)''')
#c.execute("INSERT INTO acceso VALUES (1,'lgnome35@gmail.com','H1cc$43*')")
#conn.commit()
#c.execute("INSERT INTO acceso VALUES (2,'ccidbcomputacion12@gmail.com','H1cc$43*')")
#conn.commit()
##########################################################################################################

seccion=dict()
for row in c.execute('SELECT * FROM acceso'):
	#print(row[1])>Usuario
	#print(row[2])>Password
	seccion.update({row[0]:{'users':row[1],'password':row[2]}})
conn.close()


def main():
	###############tiempo random!##################
	TR=lambda:int(rd(50,350)*2+9)+(rd(0,100)/3+100)
	###############################################
	try:
		
		def megaFaker():			
			with open('1000.json', 'r') as milSemillas:
				milSemillas=js(milSemillas)
			categoria =[
					"animal",
					"carmodle",
					"moviesTitle",
					"NameOfCompany",
					"uni",
					"apps"
					]
			rCategoria  = (str(categoria[rd(0,(len(categoria))-1)]))   
			#####################Entrenar IA mejor dese txt#############
			if(rCategoria=="animal"):
				palabras=[
					"donde encontar ",
					"habita ",
					"comida ",
					"peloigro de extinción ",
					"venenoso ",
					"composicion osea ",
					]    
			elif(rCategoria=="carmodle"):
				palabras=[
					"que es  ",
					"a que sabe ",
					"donde queda ",
					"como encontrar ",
					"ver "]    
			elif(rCategoria=="moviesTitle"):
				palabras=[
					"fecha de lanzamiento de ",
					"reparto  en ",
					"secuelas de  ",
					"resumen  ",
					"protagonista en ",
					"elenco de ",
					"descargar de ",
					"animacion de ",
					"calidad  de " ,
					"cinematic de ",
					"musica de " ,
					"esenario en ", 
					"Historia en"  ,
					"catetgoria de la " ,
					"errores de la " ,
					"trama de" ,
					"arte de " ,
					"libro de " ,
					"escritor de " ,
					"gion de " ,
					"etapas de ",
					]    
			elif(rCategoria=="NameOfCompany"):
				palabras=[
					"fecha de creacion ",
					"competencia de la ",
					"estrategia de la ",
					"vision  de la ",
					"mision de la ",
					"capacidad de trabajadores ",
					"beneficios de la ",
					]   
			elif(rCategoria=="uni"):
				palabras=[
					"requisitos para entara en ",
					"carrera ",
					"donde queda la ",
					"como encontrar la ",
					"que hacer en la ",
					"obtener beca en la "
					]    
			if(rCategoria=="apps"):
				palabras=[
					"Version ",
					"git ",
					"licencia ",
					"como encontrar ",
					"que hacer en la ",
					"animacion ",
					"keys ",
					"free ",
					"gratis ",
					"obtener ",
					"descargar "
					]        
			  
			rSemilla     = np(milSemillas)[rd(0,999)][rCategoria]
			rPalabras    = str(palabras[rd(0,(len(palabras))-1)])			
			return(str(rPalabras+rSemilla))
		
		options = Options()#<--------------------Hiden Browser
		options.add_argument("--headless")
		driver = webdriver.Firefox(options=options,executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox')
		#driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox')
		driver.get("https://www.presearch.org/login");
		#cantidad = (len(palabras))
		
		def buscar():
			for x in range(0, 30):
				elemT = driver.find_elements_by_class_name("tour-balance")         			
				for inicioBalance in elemT:print("-----------------------++:\n"+(inicioBalance.text))
				cb = driver.find_element_by_name("term")
				cb.send_keys(megaFaker())
				t.sleep((TR()/60)/2)
				bn = driver.find_element_by_css_selector("button.rounded").click()
				t.sleep(TR()/60)
				driver.back()
				driver.refresh()
				t.sleep(2)	

		for x in seccion:
			username_field = driver.find_element_by_name("email");password_field = driver.find_element_by_name("password")
			login_button = driver.find_element_by_css_selector('button.btn-primary')
			username_field.send_keys(seccion[x]['users'])
			t.sleep(2)
			password_field.send_keys(seccion[x]['password'])
			t.sleep(3)
			login_button.click()
			t.sleep(3)
			elem = driver.find_elements_by_class_name("tour-balance")         
			
			for inicioBalance in elem:
				print("-----------------------\n"+str(x)+")Usuario: ["+seccion[x]['users']+"] Acomulado: {"+(inicioBalance.text)+"}")	
			buscar()
			elemD = driver.find_elements_by_class_name("tour-balance")        
 			
			for finalBalance in elemD:
				f = finalBalance.text
				final=1000.00-(float(f.replace("PRE", "", 3)))
				print("Final obtenido: {"+(finalBalance.text)+"}")
				print("Total tokens Faltante: {"+str(final)+"}")
			driver.close();driver = webdriver.Firefox(options=options,executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox');driver.get("https://www.presearch.org/login")
			#driver.close();driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',firefox_binary='/usr/bin/firefox');driver.get("https://www.presearch.org/login")

		driver.close()
		
	except Exception as e: print(e)
if __name__ == '__main__':
	main()
#descaomentar para mostrar el contenido de la paguina 
#html = driver.page_source
