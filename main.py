number_card = input("Введите номер карты")
"""Проверка номера карты на корректность"""

if not number_card.isdigit() or len(number_card) != 16:
    print("Некорректный номер карты")

account = input("Введите номер счёта")
"""Проверка номера счёта на корректность"""

if not account.isdigit() or len(account) !=20:
    print("Некорректный номер счёта")