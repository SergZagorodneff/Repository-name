# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    letter_number = {}
    for char in text:
        if char.isalpha():
            letter_number[char] = letter_number.get(char, 0) + 1
    return letter_number

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_number):
    total_letters = sum(letter_number.values())
    frequency_dict = {}
    for letter, number in letter_number.items():
        frequency_dict[letter] = round(number / total_letters,2)
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_number = count_letters(main_str)
frequency_dict = calculate_frequency(letter_number)
# TODO Распечатайте в столбик букву и её частоту в тексте
for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")