import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://www.divan.ru/sankt-peterburg/category/svet'
driver.get(url)
time.sleep(3)

svetilniks = driver.find_elements(By.CLASS_NAME,'wYUX2')

parsed_data = []
for svetilnik in svetilniks:
    try:
        title = svetilnik.find_element(By.CSS_SELECTOR,'a.ui-GPFV8').text
        newprice = svetilnik.find_element(By.CSS_SELECTOR,'span.ui-LD-ZU.KIkOH').text
        oldprice = svetilnik.find_element(By.CSS_SELECTOR,'span.ui-LD-ZU.ui-SVNym.bSEDs').text
        link = svetilnik.find_element(By.CSS_SELECTOR,'a.ui-GPFV8').get_attribute('href')

    except:
       print("произошла чудовищная ошибка")
       continue
    parsed_data.append([title,newprice,oldprice,link])

driver.quit()

with open("svetilniks.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название модели светильника', 'Новая цена', 'Старая цена', 'ссылка на товар'])
    writer.writerows(parsed_data)
print(parsed_data)
