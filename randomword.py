import requests
from bs4 import BeautifulSoup

from googletrans import Translator

def get_english_word():
    url = "https://randomword.com"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()

        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Ошибка {e}")
        return None

translator = Translator()

def word_game():
    print("Welcome!")
    while True:
        word_dict = get_english_word()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        ru_word= translator.translate(word, dest="ru")
        ru_definition = translator.translate(word_definition, dest="ru")
        print(ru_definition.text)
        print(f"Значение слова {ru_definition.text}")
        user = input("Что это за слово?")
        if user ==ru_word.text:
            print("Все верно")
        else:
            print(f"Ответ неверный, было загадано слово {ru_word.text}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again!="y":
            print("Спасибо за игру")
            break      
word_game()               

