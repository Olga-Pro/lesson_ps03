# Сейчас игра получает английское слово и английское определение.
# Сделайте так, чтобы слова и определения этих слов были на русском.
# Для этого понадобится модуль googletrans.

import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words_and_translate():
    # функция для получения информации
    url = "https://randomword.com/"

    translator = Translator()  # Для перевода на русский язык

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()  # получить слово + удалить все пробелы
        russian_word = translator.translate(english_word, dest="ru").text

        word_definition = soup.find("div", id="random_word_definition").text.strip()  # описание слова
        russian_definition = translator.translate(word_definition, dest="ru").text

        return {
            "english_words": english_word,
            "word_definitions": word_definition,
            "russian_words": russian_word,
            "russian_definitions": russian_definition
                }
    except:
        print("Произошла ошибка")


def word_game():
    # Игра: угадать слово по описанию

    print("Добро пожаловать в игру!")
    variant = input("Играем на русском или английском языке? r/e ")

    while True:
        word_dict = get_english_words_and_translate()

        if variant.upper() == "R":
            word = word_dict.get("russian_words")
            word_definition = word_dict.get("russian_definitions")
        else:
            word = word_dict.get("english_words")
            word_definition = word_dict.get("word_definitions")

        # Игра:
        print(f"Значение слова: {word_definition}")
        user_word = input("Что это за слово? ")
        if user_word.upper() == word.upper():
            print("Верно!")
        else:
            print(f"Ответ неверный, загадано слово - {word}")

        # Возможность закончить игру:
        play_again = input("Хотите сыграть еще? y/n ")
        if play_again.upper() != "Y":
            print("Спасибо за игру!")
            break


word_game()
