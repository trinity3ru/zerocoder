import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://kwork.ru/categories/textgeneration/ii-generatsiya-statey"
driver.get(url)
time.sleep(5)

orders = driver.find_elements(By.CSS_SELECTOR, ".kwork-card-item")
print(f"Orders: {len(orders)}")
parsed_data = []

for order in orders:
    try:
        title_element = order.find_element(By.CSS_SELECTOR, ".first-letter")
        title = title_element.text
        link_element = order.find_element(By.CSS_SELECTOR, ".kwork-card-item__title a")
        link = link_element.get_attribute("href")
        price = order.find_element(By.CSS_SELECTOR, ".kwork-cards-price__volume").text.strip()
        print(title, link, price)
    except Exception as e:
        print(f"Ошибка при обработке заказа: {e}")
        continue

    parsed_data.append([title, link, price])

with open("kwork.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Предложение", "Ссылка", "Цена за 1000 символов"])
    writer.writerows(parsed_data)

driver.quit()
