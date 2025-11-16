import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://en.wikipedia.org/wiki/Main_Page")

def move_to_page(question:str):
    

    search_box = browser.find_element(By.XPATH, '//input[@id="searchInput"]')

    search_box.send_keys(question)

    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    print(f" We had moved to {browser.title}")

def choose_link(links:str):
    for i, link_el in  enumerate(links):
            print (f"{i}. {link_el.text} ")

            
    number = int(input("Choose number of the link to move"))
    target = links[number].get_attribute("href")
    print(f"Переходим: {target}")
    browser.get(target)
       

while True:
    question = input("What will we search in Wiki?")
    move_to_page(question)


    if 'Search' in browser.title: #если search в title значит перешли не на страницу а в результаты поиска и выбираем куда дальше
        search_results = browser.find_elements(By.CLASS_NAME,'mw-search-result-heading')
        print(f"search results {len(search_results)}")
        links = [search_result.find_element(By.TAG_NAME,"a") for search_result in search_results]
        print(f"links {len(links)}")
        if links:
            choose_link(links) 
        else:
            print(f"Found nothing about {question} in Wiki")
            exit
            
    while True: #внутренний цикл на работу со статьей
        action = input("Enter or any key - scroll text, m- move to the linked article, q- quit")
        
        if action == 'm':

            links = []
            article = browser.find_element(By.ID,'mw-content-text')
            links = [
                a for a in article.find_elements(By.CSS_SELECTOR, "#mw-content-text a") if a.text.strip() and a.get_attribute("href") and a.get_attribute("href").startswith("http")    
                     ]
            # mw-content-text
            # mw-content-ltr mw-parser-output
            if links:
                print(f"Найдено ссылок: {len(links)}")
                choose_link(links) 
 
            else:
                print("Нет ссылок на этой странице.")
                browser.save_screenshot("no-links.png")

        if action == 'q':
            break
                    
        else:
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                scroll = input("Enter to scroll, q - for quit reading")
                if scroll == 'q':
                    break    
 

time.sleep(1)
browser.quit()