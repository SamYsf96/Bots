from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

link = input("Please copy and paste the link.")
driver.get(link)
addToCart = driver.find_element_by_id("add-to-cart-button")
addToCart.click()
driver.find_element_by_id("nav-cart-count").click()
driver.implicitly_wait(5)
driver.find_element_by_name("proceedToRetailCheckout").click()
email = driver.find_element_by_id("ap_email")
email.send_keys("soroush.y96@gmail.com")
email.send_keys(Keys.ENTER)
pw = driver.find_element_by_id("ap_password")
pw.send_keys("panzer12765")
pw.send_keys(Keys.ENTER)