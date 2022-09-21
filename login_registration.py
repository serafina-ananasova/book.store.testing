# # registratin account
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# # time.sleep(5)
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# registration_email = driver.find_element_by_id("reg_email")
# registration_email.send_keys("sima-26.05@mail.ru")
# registration_password = driver.find_element_by_id('reg_password')
# registration_password.send_keys('134679258Bol!sima')
# register = driver.find_element_by_css_selector('p.woocomerce-FormRow.form-row > input.woocommerce-Button.button').click()
# driver.quit()

# login
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
username = driver.find_element_by_id('username')
username.send_keys('sima-26.05@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('134679258Bol!sima')
login = driver.find_element_by_css_selector('p:nth-child(3) > input.woocommerce-Button.button').click()
logout_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li > a[href="https://practice.automationtesting.in/my-account/customer-logout/"]')))