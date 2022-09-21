# # book of the name
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id('username')
# username.send_keys('sima-26.05@mail.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('134679258Bol!sima')
# login = driver.find_element_by_css_selector('p:nth-child(3) > input.woocommerce-Button.button').click()
# shop = driver.find_element_by_id('menu-item-40').click()
# book_html5_forms = driver.find_element_by_css_selector('div#content li:nth-child(3) h3').click()
# name_of_the_book = driver.find_element_by_class_name('product_title.entry-title ')
# name_of_the_book_get_text = name_of_the_book.text
# assert name_of_the_book_get_text =='HTML5 Forms'

# # 3 product
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id('username')
# username.send_keys('sima-26.05@mail.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('134679258Bol!sima')
# login = driver.find_element_by_css_selector('p:nth-child(3) > input.woocommerce-Button.button').click()
# shop = driver.find_element_by_id('menu-item-40').click()
# html = driver.find_element_by_css_selector('div#woocommerce_product_categories-2 li:nth-child(2) a').click()
# product = driver.find_elements_by_css_selector('div#content li h3')
# if len(product) ==3:
#     print('3 product')
# else:
#     print('Error')

# #sorting
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id('username')
# username.send_keys('sima-26.05@mail.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('134679258Bol!sima')
# login = driver.find_element_by_css_selector('p:nth-child(3) > input.woocommerce-Button.button').click()
# shop = driver.find_element_by_id('menu-item-40').click()
# selector = driver.find_element_by_class_name('orderby')
# selector_defult_sorting = selector.get_attribute("value")
# print(selector_defult_sorting)
# if selector_defult_sorting == 'menu_order':
#     print('Сортировка по умолчанию')
# else:
#     print('Иная сортировка')
# price = Select(selector)
# price.select_by_value('price-desc')
# selector_two = driver.find_element_by_class_name('orderby')
# selector_high_low_sorting = selector_two.get_attribute("value")
# print(selector_high_low_sorting)
# if selector_high_low_sorting == 'price-desc':
#     print('Сортировка по возрастанию')
# else:
#     print('Иная сортировка')

# # wait close
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id('username')
# username.send_keys('sima-26.05@mail.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('134679258Bol!sima')
# login = driver.find_element_by_css_selector('p:nth-child(3) > input.woocommerce-Button.button').click()
# shop = driver.find_element_by_id('menu-item-40').click()
# book_android = driver.find_element_by_css_selector('div#content li:nth-child(1) h3').click()
# old_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# new_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# img = driver.find_element_by_class_name('attachment-shop_single.size-shop_single.wp-post-image').click()
# close = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) ).click()

# # buy book in the basket
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40').click()
# html5_add_to_basket = driver.find_element_by_css_selector('ul>li:nth-child(4) a[rel="nofollow"] ').click()
# time.sleep(4)
# products_in_basket = driver.find_element_by_class_name('cartcontents')
# products_in_basket_get_text = products_in_basket.text
# assert products_in_basket_get_text == "1 Item"
# price_in_basket = driver.find_element_by_css_selector('ul#main-nav>li:nth-child(6) span.amount')
# price_in_basket_get_text = price_in_basket.text
# assert price_in_basket_get_text == "₹180.00"
# basket = driver.find_element_by_class_name('wpmenucart-contents').click()
# subtotal = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'td[data-title="Subtotal"] span.woocommerce-Price-amount.amount'), '180.00'))
# total = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.cart_totals td[data-title="Total"] span.woocommerce-Price-amount.amount'), '183.60'))

# # job in basket
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5_add_to_basket = driver.find_element_by_css_selector('ul>li:nth-child(4) a[rel="nofollow"] ').click()
# time.sleep(3)
# js_add_to_basket = driver.find_element_by_css_selector('ul>li:nth-child(5) a[rel="nofollow"]').click()
# basket = driver.find_element_by_class_name('wpmenucart-contents').click()
# time.sleep(3)
# delete = driver.find_element_by_css_selector('div.woocommerce tr:nth-child(2) td.product-remove a').click()
# time.sleep(3)
# undo = driver.find_element_by_css_selector('div.woocommerce-message a').click()
# quantity = driver.find_element_by_css_selector('tr:nth-child(2) > td.product-quantity > div > input')
# quantity.clear()
# quantity.send_keys('3')
# update_basket = driver.find_element_by_css_selector('.button[value="Update Basket"]').click()
# time.sleep(3)
# quantity_new = driver.find_element_by_css_selector('tr:nth-child(2) > td.product-quantity > div > input')
# quantity_new_value = quantity_new.get_attribute('value')
# assert quantity_new_value == '3'
# time.sleep(3)
# apply_coupon = driver.find_element_by_css_selector('.button[value="Apply Coupon"]').click()
# message = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-error'), 'Please enter a coupon code.'))

# buy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
html5_add_to_basket = driver.find_element_by_css_selector('ul>li:nth-child(4) a[rel="nofollow"] ').click()
time.sleep(3)
basket = driver.find_element_by_class_name('wpmenucart-contents').click()
# proceed_to_checkout = driver.find_element_by_class_name('checkout-button.button.alt.wc-forward').click()
proceed_to_checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button.button.alt.wc-forward')))
proceed_to_checkout.click()
first_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name.send_keys('Sima')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Bolotnikova')
email_address = driver.find_element_by_id('billing_email')
email_address.send_keys('sima-26.05@mail.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89874589651')
country = driver.find_element_by_id('select2-chosen-1').click()
coutry_select = driver.find_element_by_id('s2id_autogen1_search')
coutry_select.send_keys('aus')
click_country = driver.find_element_by_css_selector('#select2-results-1 > li:nth-child(1)')
click_country.click()
address = driver.find_element_by_css_selector('input#billing_address_1')
address.send_keys('street Volskay')
suburb = driver.find_element_by_css_selector('#billing_city.input-text')
suburb.send_keys('Saratov')
state = driver.find_element_by_id('s2id_billing_state').click()
selector_state = driver.find_element_by_css_selector('#select2-results-2 > li:nth-child(1)').click()
postcode = driver.find_element_by_css_selector('#billing_postcode.input-text')
postcode.send_keys('1458756')
driver.execute_script("window.scrollBy(0, 600);")
check_payments = driver.find_element_by_id('payment_method_cheque').click()
place_order = driver.find_element_by_id('place_order').click()
test1 = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
test2 = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr:nth-child(3) > td'), "Check Payments"))

