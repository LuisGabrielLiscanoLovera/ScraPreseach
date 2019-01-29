import time as t
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
email = "luisthemaster3@gmail.com"
password = "H1cc$43*"

def main():
	#login-in
	try:
		binary = FirefoxBinary('/usr/bin/firefox')
		driver = webdriver.Firefox(firefox_binary=binary)
		driver.get("https://www.presearch.org/login")
		username_field = driver.find_element_by_name("email")
		password_field = driver.find_element_by_name("password")
		login_button = driver.find_element_by_css_selector('button.btn-primary')
		username_field.send_keys(email)
		password_field.send_keys(password)
		login_button.click()
		t.sleep(2)
		elem = driver.find_elements_by_class_name("tour-balance")
		for banlance in elem:
			print (banlance.text)
	except Exception as e: print(e)


if __name__ == '__main__':
	main()


#descaomentar para mostrar el contenido de la paguina 
#html = driver.page_source





