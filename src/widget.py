from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""

    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    if len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
        return result


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_data(data: str) -> str:
    """Функций, которая принимает на вход строку и отдает корректный результат в формате
11.07.2018"""
    new_data = data[0:10].split("-")
    return "-".join(new_data[::-1])


print(get_data("2024-03-11T02:26:18.671407"))