# Project_1

Автор: Зверева Анна Дмитриевна 

ИСУ: 335068

## Описание программы
Программа реализует шифр Виженера, который является одним из методов полиалфавитного шифрования. Она позволяет зашифровать или расшифровать введенный текст с использованием ключевого слова, а также добавляет элемент визуального разнообразия благодаря динамическому выбору цветов.

Каждый символ текста сдвигается на определенное количество позиций в алфавите, соответствующее позиции символа ключа. Если символ ключа — гласная, сдвиг происходит вправо, если согласная — влево. 

Ключевое слово анализируется на наличие гласных и согласных. Если количество гласных больше или равно количеству согласных, буквы в слове-результате будут раскрашены поочередно в цвета радуги. В противном случае буквы в слове-результате будут раскрашены фиолетовый и зеленый, чередуя эти цвета.

## Примеры имспользования:
При запуске программы вам будет предложено ввести текст и ключ, а также выбрать действие (зашифровать или расшифровать). Ниже приведены примеры ввода и вывода. Цвета могут различаться в зависимости от используемого терминала.

Пример 1:

Введите текст:
hello world

Введите ключ:
secret

Выберите действие:
1. Зашифровать
2. Расшифровать

1

Вывод: zincs pgvnu

Пример 2:

Введите текст:
Hello wor1d!

Введите ключ:
ice

Выберите действие:
1. Зашифровать
2. Расшифровать

2

Вывод: Zchdm sgp1z!
