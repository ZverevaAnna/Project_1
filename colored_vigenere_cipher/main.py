"""Основной модуль программы для шифрования и расшифровки текста с использованием шифра Виженера."""

import sys

sys.path.append('.')

from utils import (
    is_vowel,
    count_vowels_and_consonants,
    get_color_sequence,
    apply_colors_to_result,
    vigenere_cipher
)
from colorama import Fore, Style, init

init(autoreset=True)


def main():
    """
    Главная функция программы: управляет процессом взаимодействия с пользователем и вызовом функций шифрования/расшифровки.
    """
    print("Введите текст:")
    text = input().strip()

    print("Введите ключ:")
    key = input().strip()

    while True:
        print("Выберите действие:\n1. Зашифровать\n2. Расшифровать")
        choice = int(input())

        if choice == 1:
            result = vigenere_cipher(text, key, 'encrypt')
            break
        elif choice == 2:
            result = vigenere_cipher(text, key, 'decrypt')
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

    vowel_count, consonant_count = count_vowels_and_consonants(key)
    colors = get_color_sequence(vowel_count, consonant_count)
    colored_result = apply_colors_to_result(result, colors)

    print(colored_result)


if __name__ == "__main__":
    main()