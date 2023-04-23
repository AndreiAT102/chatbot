'''import random

text = input() # ввод данных от пользователя
if text in ["Привет", "Здарова", "Хеллоу"]:
    print(random.choice(["Здрасте", "Йоу", "Приветики"])) # выбор случайног элемента из ответов
elif text in ["Пока", "Увидимся", "Чао"]:
    print(random.choice(["Буду ждать нашей встречи", "Ок", "Бай-бай"])) # выбор случайног элемента из ответов
else:
    print("Не понял") # вывод на экран'''



import re # Regular Expressions
import nltk
# Filter_text - фильтр текста
# "Привет => "привет"
# "привет !!! :)" => "привет"
# "  привет  " => "привет"
def filter_text(text):
    text = text.lower() # lower - к нижнему регистру
    text = text.strip() # strip - вырезать пробелы с начала и конца строки
    pattern = r"[^\w\s]" # Все что не слово и не пробел
    text = re.sub(pattern, "", text) # Из переменной text вырезаем "Все что не слово и не пробел"
    return text

# print(filter_text(' Привет!!!  :) ')) # Проверяем функцию filter_text
def text_match(user_text, exampie):
# True, если тексты похожи (user_text пользовательский текст, exampie - контрольная фраза)
# False, если не похожи
    user_text = filter_text(user_text) # Отфильтруем лишнее из первой строки
    exampie = filter_text(exampie) # Отфильтруем лишнее из строки
    if user_text == exampie: # Если тексты точно совпадают
        return True
    if user_text.find(exampie) != -1: # Если фраза входит в пользовательский текст
        return True
    distance = nltk.edit_distance(user_text, exampie)
    # Отношение кол-ва ошибок к длине слова, 1.0 - слово целиком другое, 0 - слова полностью совпадают
    ratio = distance / len(exampie)
    if ratio < 0.40:
        return True

    return False


# Составим карты "намерений", которые поддерживает наш бот
INTENTS = {
    "hello": {
        "example": ["Привет", "Здравствуйте", "Добрый день"],
        "response": ["Йоу", "Здарова", "Приветствую тебя, человек."],
    },
    "bye": {
        "example": ["Пока", "До свидания", "Всего хорошего"],
        "response": ["Давайдосвиданья", "И Вам приятного денечка", "Чао"],
    },
    "how_are_you": {
        "example": ["Привет", "Здравствуйте", "Добрый день"],
        "response": ["Йоу", "Здарова", "Приветствую тебя, человек."],
    },
}
    
