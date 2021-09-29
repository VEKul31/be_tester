# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# time.sleep(3)
# driver.get('https://google.ru')
# time.sleep(3)
# textfield = driver.find_element_by_xpath("//input[@name='q']")
# textfield.send_keys("погода на завтра")
# time.sleep(3)
# submit_button = driver.find_element_by_xpath("//div[@jsname='VlcLAe']//input[@class='gNO89b']")
# submit_button.click()
# time.sleep(3)
# driver.quit()
# import time
#
# from selenium import  webdriver
#
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%D0%A3%D1%87%D1%91%D0%B1%D0%B0/%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/2%20%D0%A3%D1%80%D0%BE%D0%BA/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D1%81%20%D1%81%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%BC.html')
# elementByLinkText = driver.find_element_by_link_text('Перейти к содержимому')
# elementByPartialLinkText = driver.find_element_by_partial_link_text('Пере')
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
# PIM = driver.find_element_by_id('menu_pim_viewPimModule')
# PIM.click()
# Add = driver.find_element_by_id('menu_pim_addEmployee')
# time.sleep(3)
# Add.click()
# FN = driver.find_element_by_id('firstName')
# FN.send_keys('Sheldon')
# LN = driver.find_element_by_id('lastName')
# LN.send_keys('London')
# Save = driver.find_element_by_id('btnSave')
# Save.click()
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
# PIM = driver.find_element_by_id('menu_pim_viewPimModule')
# PIM.click()
# List = driver.find_element_by_id('menu_pim_viewEmployeeList')
# List.click()
# EN = driver.find_element_by_name('empsearch[employee_name][empName]')
# time.sleep(3)
# EN.click()
# EN.send_keys('Sheldon London')
# Search = driver.find_element_by_name('_search')
# Search.click()
# CB = driver.find_element_by_class_name('checkbox-col')
# CB.click()
# Delete = driver.find_element_by_name('btnDelete')
# Delete.click()
# Ok = driver.find_element_by_css_selector('.btn#dialogDeleteBtn')
# Ok.click()
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.rushplace.com/")
# time.sleep(3)
# One = driver.find_element(By.XPATH,"//*[@data-product_id='44']")
# One.click()
# time.sleep(1)
# Two = driver.find_element(By.XPATH,"//*[@data-product_id='63']")
# Two.click()
# time.sleep(1)
# Three = driver.find_element(By.XPATH,"//*[@data-product_id='40']")
# Three.click()
# time.sleep(1)
# Basket = driver.find_element(By.CSS_SELECTOR, 'span.subtotal')
# Basket.click()
# time.sleep(1)
# items_count = driver.find_elements(By.CSS_SELECTOR, 'td.product-name')
# if len(items_count) == 3:
#     print('В корзине 3 товара')
# else:
#     print('Ошибка.Количество товаров в корзине:'+str(len(items_count)))
# driver.quit()