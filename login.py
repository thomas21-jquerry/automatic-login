from selenium import webdriver
import time


driver = webdriver.Chrome()
username = "user@phptravels.com"
password = "demouser"
driver.get("https://www.phptravels.net/login")
driver.maximize_window()
print("your automation is running... ")

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath("//button[@class = 'btn btn-primary btn-lg btn-block loginbtn'][@type = 'submit']").click()

print("login successful :)")
driver.quit()

