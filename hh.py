import time
import csv
import pprint
from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'https://tyumen.hh.ru/vacancies/programmist'

driver.get(url)
time.sleep(5)

parser_date = []

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-info--umZA61PpMY07JVJtomBA')

for vacencie in vacancies:
    # try:
    title = vacencie.find_element(By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]').text
    company = vacencie.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
    salary = vacencie.find_element(By.XPATH, '//span[@data-sentry-element="Text" and @data-sentry-component="Compensation"]').text
    # salary = vacencie.find_element(By.CSS_SELECTOR, 'span.[data-sentry-component="Compensation"]').text
    link = vacencie.find_element(By.CSS_SELECTOR, 'a[data-qa="serp-item__title"]').get_attribute('href')
    # link = link2.get_attribute('href')
    # link = vacencie.find_element(By.TAG_NAME, 'a.magritte-link___b4rEM_4-3-8').get_attribute('href')
    # except Exception as e:
    #     print("Error")
    #     continue

    parser_date.append([title, company, salary, link])
    # parser_date.append([title, company, salary])


driver.quit()



with open("hh.csv", "w", newline='' ,encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Заголовок', 'Компания', 'Зарплата', 'Ссылка'])
    # writer.writerow(['Заголовок', 'Компания', 'Зарплата'])
    writer.writerows(parser_date)
    print("Файл hh.csv сформирован")


