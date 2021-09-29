# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
# Leave = driver.find_element_by_id('menu_leave_viewLeaveModule')
# Leave.click()
# Leavelist = driver.find_element_by_id('menu_leave_viewLeaveList')
# Leavelist.click()
# P_A = driver.find_element_by_id("leaveList_chkSearchFilter_1")
# P_A_c = P_A.get_attribute('checked')
# print('value of P_A_C:', P_A_c)
# if    P_A_c is not None:
#     print('Чекбокс отмечен')
# else:
#     print('Чекбокс НЕ отмечен')
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
# Leave = driver.find_element_by_id('menu_leave_viewLeaveModule')
# Leave.click()
# Leavelist = driver.find_element_by_id('menu_leave_viewLeaveList')
# Leavelist.click()
# Sheduled = driver.find_element_by_id("leaveList_chkSearchFilter_2")
# SheduledChek = Sheduled.get_attribute('checked')
# print('value of SheduledChek:', SheduledChek)
# if    SheduledChek is None:
#     print('Атрибута нет')
# else:
#     print('Атрибут есть')
# driver.quit()

# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_
# select = Select(element)
# select.select_by_value("")
# select.select_by_visible_text("text") #ищет элемент по видимому тексту
# select.select_bu_index(index) #ищет элемент по его индексу или порядковому номеру. Число, без кавычек

# ДЗ 1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_name("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_name("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_name("Submit")
# login_btn.click()
#
# PIM = driver.find_element_by_id('menu_pim_viewPimModule')
# PIM.click()
# EmpList = driver.find_element_by_id('menu_pim_viewEmployeeList')
# EmpList.click()
#
# Name = driver.find_element_by_link_text('Peter Mac')
# Name.click()
# Female = driver.find_element_by_id('personal_optGender_2')
# Female_checked = Female.get_attribute('disabled')
# print('Переключатель на женский пол:', Female_checked)
# if    Female_checked is not None:
#     print('Выбор недоступен')
# else:
#     print('Выбор доступен')
#
# Nationality = driver.find_element_by_id('personal_cmbNation')
# Nat_checked = Nationality.get_attribute('disabled')
# print('Выбор национальности:', Nat_checked)
# if    Nat_checked is not None:
#     print('Выбор недоступен')
# else:
#     print('Выбор доступен')
#
# Edit = driver.find_element_by_id('btnSave')
# Edit.click()
# time.sleep(1)
#
# NotMale = driver.find_element_by_id('personal_optGender_2')
# NotMale.click()
# time.sleep(1)
# Female_checked = Female.get_attribute('checked')
# print('Выбран ли пол:', Female_checked)
# if    Female_checked is not None:
#     print('Радиокнопка выбрана')
# else:
#     print('Радиокнопка не выбрана')
#
# from selenium.webdriver.support.select import Select
# Nationality = driver.find_element_by_id('personal_cmbNation')
# select = Select(Nationality)
# select.select_by_value('193')
# time.sleep(1)
# Nat_checked = Nationality.get_attribute('value')
# print('Какая страна по счёту:', Nat_checked)
# if    Nat_checked == "193":
#     print('Выбрана последняя страна')
# else:
#     print('Выбрана не последняя страна')
#
# Male = driver.find_element_by_id('personal_optGender_1')
# Male.click()
# time.sleep(1)
# select.select_by_value('0')
# time.sleep(1)
# Edit.click()
# time.sleep(2)
# driver.quit()

# file = ('D:\Учёба\Тестирование\Автоаматизация\3 Урок\picture.jpg')
# upload = driver.find_element_by_id('upload_btn')
# upload.send_keys(file) #Задание 2.4

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.execute_script('alert("Скрипт выполнен успешно!");')

# button = driver.find_element_by_tag_name('button')
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# button. click() #or
# driver.execute_script("window.scrollBy(0,100);") #Задание 2.5
# current_page = driver.current_url
# print(current_page) #выведет адрес ссылки на которой мы находимся
# driver.find_element_by_css_selector("option:nth-child(2)").click()
# driver.find_element_by_css_selector("[value='4']").click()

# ДЗ 2
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://demo.automationtesting.in/Register.html")
#
# FN = driver.find_element_by_css_selector('[placeholder="First Name"]')
# FN.click()
# FN.send_keys('Vsevolod')
#
# LN = driver.find_element_by_css_selector('[placeholder="Last Name"]')
# LN.click()
# LN.send_keys('Kulakov')
#
# Eadress = driver.find_element_by_css_selector('[type="email"]')
# Eadress.click()
# Eadress.send_keys('Sev7715@gmail.com')
#
# Phone = driver.find_element_by_css_selector('[type="tel"]')
# Phone.click()
# Phone.send_keys('1234554321')
#
# Male = driver.find_element_by_css_selector('[value="Male"]')
# Male.click()
#
# from selenium.webdriver.support.select import Select
# Country = driver.find_element_by_id('countries')
# selectC = Select(Country)
# selectC.select_by_value('Russia')
#
# Year = driver.find_element_by_id('yearbox')
# selectY = Select(Year)
# selectY.select_by_value('1995')
#
# Month = driver.find_element_by_css_selector('[placeholder="Month"]')
# selectM = Select(Month)
# selectM.select_by_value('July')
#
# Day = driver.find_element_by_id('daybox')
# selectD = Select(Day)
# selectD.select_by_value('24')
#
# Password = driver.find_element_by_id('firstpassword')
# Password.click()
# Password.send_keys('At09092021')
#
# CPassword = driver.find_element_by_id('secondpassword')
# CPassword.click()
# CPassword.send_keys('At09092021')
#
# Photo = ('D:\Учёба\Тестирование\Автоматизация\Я.jpg')
# upload = driver.find_element_by_id('imagesrc')
# upload.send_keys(Photo)
# time.sleep(1)
# driver.execute_script("window.scrollBy(0,300);")
# time.sleep(1)
#
# Submit = driver.find_element_by_id('submitbtn')
# Submit.click()
# time.sleep(2)
#
# current_page = driver.current_url
# if    current_page == 'http://demo.automationtesting.in/WebTable.html':
#     print('Переход состоялся')
# else:
#     print('Переход не состоялся')
# driver.quit()

# 3 тема
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# alert_script = driver.execute_script("alert('Скрипт выполнен успешно!');")
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# alert.accept()

# confirm = driver.switch_to.alert
# confirm.accept()
# confirm.dismiss()

# prompt = driver.switch_to.alert
# prompt.send_keys("Prompt")
# prompt.accept() or dismiss()

# driver.switch_to.window(window_name)
# new_window = driver.window_handles[1] # Поиск и взаимодействие будут происходить уже на новой странице
# current_window = driver.current_window_handle
# driver.execute_script("window.open();")

# ДЗ 3
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# Switch_To = driver.find_element_by_link_text('SwitchTo')
# Switch_To.click()
# Alerts = driver.find_element_by_link_text('Alerts')
# Alerts.click()
# Red_button = driver.find_element_by_css_selector('[class = "btn btn-danger"]')
# time.sleep(1)
# Red_button.click()
#
# alert = driver.switch_to.alert
# alert_text = alert.text
# if   alert_text == 'I am an alert box!':
#     print('Содержимое равно')
# else:
#     print('Ошибка')
# print(alert_text)
# alert.accept()
#
# current_page = driver.current_url
# print(current_page)
# driver.execute_script("window.open();")
# window_after = driver.window_handles[2]
# driver.switch_to.window(window_after)
# time.sleep(1)
# driver.get(current_page)
# time.sleep(1)
#
# Alert_with_OKCancel = driver.find_element_by_link_text('Alert with OK & Cancel')
# Alert_with_OKCancel.click()
# time.sleep(1)
# Blue_button = driver.find_element_by_css_selector('[class = "btn btn-primary"]')
# Blue_button.click()
# confirm = driver.switch_to.alert
# confirm.dismiss()
#
# driver.execute_script("window.open();")
# window_after_1 = driver.window_handles[3]
# driver.switch_to.window(window_after_1)
# time.sleep(1)
# driver.get(current_page)
# time.sleep(1)
#
# Alert_with_Textbox = driver.find_element_by_link_text('Alert with Textbox')
# Alert_with_Textbox.click()
# time.sleep(1)
# Sky_button = driver.find_element_by_css_selector('[class = "btn btn-info"]')
# Sky_button.click()
# prompt = driver.switch_to.alert
# prompt.send_keys("Ура! Задание выполнено!")
# prompt.accept()
# time.sleep(1)
#
# driver.quit()

# Тема 4

# assert element_check == "нужное нам значение"
# element = driver.find_element_by_css_selector(".card-text.second")
# element_get_text = element.text
# assert element_get_text == "Bar doggo"

# element = driver.find_element_by_css_selector(".enty-content > p")
# element_get_text = element.text
# assert "напоминает" in element_get_text

# all_checkbox = driver.find_element_by_id("select-all")
# all_checkbox_checked = all_checkbox_checked.get_attribute("checked")
# assert all_checkbox_checked is not None

# Selenium Waits. Implicit Waits. Неявное ожидание!
# driver.implicitly_wait(5) после импорта модулей, инициации webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("http://demo.automationtesting.in/Loader.html")
# run_btn = driver_find_element_by*("селектор")
# run_btn.click()
# save_changes_btn = WebDriverWait(driver, 20).until(		# говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "ваш селектор")) )
# modal_window = driver_find_element_by*("селектор")
# modal_window_text = modal_window.text
# assert "Modal title" in modal_window_text
# save_changes_btn.click()

# element_to_be_selected(element) # проверка что элемент выбран
# invisibility_of_element_located(locator) # проверка что элемент невидим
# number_of_windows_to_be(number) # проверка что количество открытых око/вкладок = заданому значению
# text_to_be_present_in_element_value(locator, text_) # проверка что текст присутствует в элементе
# url_to_be(url) # проверка что адрес страницы равен заданому значению

# button = WebDriverWait(driver, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify")) )

# wait = WebDriverWait(driver, 10) # вынесли повторяющуюся часть в переменную wait
# number_of_tabs = wait.until(EC.number_of_windows_to_be(количество ожидаемых вкладок в виде цифры)) # кавычки для цифры не нужны
# print(number_of_tabs ) # вернёт True, если количество открытых окон/вкладок в браузере = количеству ожидаемых

# ДЗ 4.1
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# More = driver.find_element(By.LINK_TEXT, "More").click()
# Loader = driver.find_element(By.LINK_TEXT, "Loader").click()
# time.sleep(1)
# Run_text = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.ID, "loader"), "Run"))
# Run = driver.find_element(By.ID, "loader").click()
#
#
# Lorem = WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-body"), "Lorem"))
# Save_changes_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick="history.go(0)"]')))
# Save_changes_btn.click()
# driver.quit()

# ДЗ 4.2
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(25)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# More = driver.find_element(By.LINK_TEXT, "More").click()
# Dynamic_Data = driver.find_element(By.LINK_TEXT, "Dynamic Data").click()
# time.sleep(3)
# The_data = driver.find_element(By.TAG_NAME,'h3')
# The_data_text = The_data.text
# assert The_data_text == 'Loading the data Dynamically'
# Get_Dynamic_Data = driver.find_element(By.ID, 'save').click()
# Get_img = driver.find_element(By.CSS_SELECTOR, '#loading img')
# Get_img_checked = Get_img.get_attribute("src")
# print(Get_img_checked)
# driver.quit()

# ДЗ 4.3
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(25)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# More = driver.find_element(By.LINK_TEXT, "More").click()
# File_Upload = driver.find_element(By.LINK_TEXT, "File Upload").click()
# file = ('D:\Учёба\Тестирование\Автоматизация\Кися.jpg')
# upload = driver.find_element(By.NAME, "input4[]")
# upload.send_keys(file)
# Remove = driver.find_element(By.CSS_SELECTOR, '[title = "Clear selected files"]').click()
#
# file_1 = ('D:\Учёба\Тестирование\Автоматизация\Пустой.txt')
# upload.send_keys(file_1)
#
# Error = driver.find_element(By.CSS_SELECTOR, '[class = "close kv-error-close"]').click()
# upload_check = upload.get_attribute('disabled')
# if upload_check is None:
#     print('Кнопка недоступна для нажатия')
# else:
#     print('Кнопка доступна')
# driver.quit()

# ДЗ 4.4
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(35)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# More = driver.find_element(By.LINK_TEXT, "More").click()
# J_PB = driver.find_element(By.LINK_TEXT, "JQuery ProgressBar").click()
#
# Wait = WebDriverWait(driver, 15)
# Close = Wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog-buttonset>[type = 'button']")))
# Star_D = driver.find_element(By.CSS_SELECTOR, "button#downloadButton")
# Star_D.click()
# C_D = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[role = 'dialog'] .ui-dialog-buttonset"), 'Cancel Download'))
# Close_1 = driver.find_element(By.CSS_SELECTOR, ".ui-dialog-buttonset>[type = 'button']").click()
# Star_D.click()
# Complete = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#dialog .progress-label"), "Complete!"))
# driver.quit()

# ДЗ 4.5
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Sev77\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(35)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#
# SwitchTo = driver.find_element(By.LINK_TEXT, "SwitchTo").click()
# Windows = driver.find_element(By.LINK_TEXT, "Windows").click()
# Click = driver.find_element(By.LINK_TEXT, "click").click()
#
# second_browser_tab = driver.window_handles[2]
# driver.switch_to.window(second_browser_tab)
# driver.close()
# driver.switch_to.window(first_browser_tab)
#
# Seperate_Multiple_Windows = driver.find_element(By.LINK_TEXT, "Open Seperate Multiple Windows").click()
# Click_1 = driver.find_element(By.CSS_SELECTOR, "[onclick = 'multiwindow()']").click()
# third_browser_tab = driver.window_handles[3]
# driver.switch_to.window(third_browser_tab)
#
# wait = WebDriverWait(driver, 10)
# addres = wait.until(EC.url_to_be('http://demo.automationtesting.in/Index.html'))
# number_of_tabs = wait.until(EC.number_of_windows_to_be(4))
# print(number_of_tabs)
#
# Email = driver.find_element(By.ID, "email")
# Email.send_keys('Sev7715@gmail.com')
# More = driver.find_element(By.ID, 'enterimg').click()
#
# addres_1 = wait.until(EC.url_to_be('http://demo.automationtesting.in/Register.html'))
# driver.quit()

# import time #Тест, 9 вопрос
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/")
# Button = driver.find_element_by_id('button')