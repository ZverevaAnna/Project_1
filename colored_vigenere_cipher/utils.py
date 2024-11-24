"""
Модуль, содержащий вспомогательные функции для работы с шифром Виженера
"""

from colorama import Fore, Style


def is_vowel(letter):
    """
    Проверяет, является ли переданная буква гласной.

    :param letter: Буква для проверки
    :return: True, если буква является гласной, иначе False
    """
    vowels = "AEIOUaeiou"
    return letter in vowels


def count_vowels_and_consonants(key):
    """
    Подсчитывает количество гласных и согласных букв в переданном ключе.

    :param key: Ключ шифрования
    :return: Количество гласных и согласных букв
    """
    vowel_count = sum(1 for k in key if is_vowel(k))
    consonant_count = len(key) - vowel_count
    return vowel_count, consonant_count


def get_color_sequence(vowel_count, consonant_count):
    """
    Возвращает последовательность цветов для окрашивания текста в зависимости от соотношения гласных и согласных.

    :param vowel_count: Количество гласных букв
    :param consonant_count: Количество согласных букв
    :return: Список цветов для окраски текста
    """
    if vowel_count >= consonant_count:
        colors = [
            Fore.RED,
            Fore.LIGHTYELLOW_EX,
            Fore.YELLOW,
            Fore.GREEN,
            Fore.BLUE,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTMAGENTA_EX
        ]
    else:
        colors = [Fore.MAGENTA, Fore.GREEN]
    return colors


def apply_colors_to_result(result, colors):
    """
    Применяет заданные цвета к каждой букве результата.

    :param result: Исходный результат шифрования/расшифровки
    :param colors: Последовательность цветов для применения
    :return: Окончательный результат с примененными цветами
    """
    colored_result = ""
    color_index = 0
    for char in result:
        colored_result += f"{colors[color_index % len(colors)]}{char}"
        color_index += 1
    return colored_result


def vigenere_cipher(text, key, mode='encrypt'):
    """
    Выполняет шифрование или расшифровку текста с использованием шифра Виженера.

    :param text: Текст для шифрования/расшифровки
    :param key: Ключ шифрования
    :param mode: Режим работы ('encrypt' для шифрования, 'decrypt' для расшифровки)
    :return: Зашифрованный или расшифрованный текст
    """

    encrypted_text = ''
    key_index = 0

    for char in text:
        if char.isalpha():
            # Получаем ASCII-код символа
            char_code = ord(char.upper())

            # Если буква строчная, то добавляем 32 к коду (чтобы привести его к верхнему регистру)
            if char.islower():
                char_code += 32

            # Получаем ASCII-код символа ключа
            key_char_code = ord(key[key_index].upper()) - ord('A')

            # Шифруем или дешифруем символ
            if mode == 'encrypt':
                new_char_code = (char_code + key_char_code) % 26 + ord('A')
            elif mode == 'decrypt':
                new_char_code = (char_code - key_char_code) % 26 + ord('A')

            # Преобразуем новый код обратно в символ
            encrypted_char = chr(new_char_code)

            # Добавляем результат в итоговую строку
            encrypted_text += encrypted_char.lower() if char.islower() else encrypted_char

            # Переходим к следующему символу ключа
            key_index = (key_index + 1) % len(key)
        else:
            # Если символ не алфавитный, просто добавляем его как есть
            encrypted_text += char

    return encrypted_text
