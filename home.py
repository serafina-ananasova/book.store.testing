import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(5)
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector("div > ul > li > a.woocommerce-LoopProduct-link > h3").click()
reviews = driver.find_element_by_css_selector("li.reviews_tab > a").click()
five_stars = driver.find_element_by_class_name("star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Sima")
email = driver.find_element_by_id("email")
email.send_keys("sima@mail.ru")
submit = driver.find_element_by_css_selector("div #submit").click()
driver.quit()