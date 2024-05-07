import datetime
import settings


# Ввод даты с проверкой формата
def enter_date() -> str:
    try:
        date = input('Введите дату (гггг-мм-дд):')
        datetime.datetime.strptime(date, settings.DATE_FORMAT)
        return date
    except ValueError:
        print("Неверный формат даты")
        return enter_date()


# Ввод суммы
def enter_amount() -> int:
    amount = input('Введите сумму (целое число): ')

    if amount.isdigit():
        return int(amount)

    else:
        print("Введите целое число")
        return enter_amount()


# Ввод категории записи с проверкой на существование категории
def enter_category() -> str:
    category = input('Введите категорию (доход/расход): ')

    if category.lower() in settings.ALLOWED_CATEGORIES:
        return category
    else:
        print("Данной категории не существует")
        return enter_category()
