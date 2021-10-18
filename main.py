from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

novel = driver.window_handles[0]
page = 'https://www.69shu.com/txt/35349/24726838'
driver.get(page)

driver.switch_to.new_window()
deepl = driver.window_handles[1]
driver.get('https://www.deepl.com/translator')
cookiebutton = driver.find_element(By.XPATH, """/html/body/div[7]/div/div/div/span/button""")
cookiebutton.click()
input_css = 'div.lmt__inner_textarea_container textarea'
input_area = driver.find_element(By.CSS_SELECTOR, input_css)
driver.switch_to.window(novel)

count = 0
transl = []

while True:
    if count == 2:
        break

    button = driver.find_element(By.CSS_SELECTOR, ".page1 > a:nth-child(4)")
    page = button.get_attribute('href')
    content = driver.find_element(By.XPATH, """/html/body/div[3]/div/div[3]""").text
    time.sleep(3)
    driver.get(page)

    driver.switch_to.window(deepl)
    input_area.clear()
    time.sleep(2)
    input_area.send_keys(content)

    while True:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.lmt__side_container--target textarea')))
        if (element.get_attribute('value') != '') and '[...]' not in element.get_attribute('value'):
            time.sleep(1)
            transl.append(element.get_attribute('value'))
            break
    driver.switch_to.window(novel)
    count += 1

print(transl)
