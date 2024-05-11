import requests
from bs4 import BeautifulSoup

def get_english_words():
    # функция для получения информации
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()  # получить слово + удалить все пробелы

        word_definition = soup.find("div", id="random_word_definition").text.strip()  # описание слова

        return {
            "english_words" : english_word,
            "word_definitions" : word_definition
        }

    except:
        print("Произошла ошибка")

def word_game():
    # Игра: угадать слово по описанию
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definitions")

        # Игра:
        print(f"Значение слова: {word_definition}")
        user_word = input("Что это за слово? ")
        if user_word == word:
            print("Верно!")
        else:
            print(f"Ответ неверный, загадано слово - {word}")

        # Возможность закончить игру:
        play_again = input("Хотите сыграть еще? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()