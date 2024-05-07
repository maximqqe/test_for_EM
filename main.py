import util
from budget_manager import BudgetManager
from record import Record


def main() -> None:
    # инициализация менеджера записей
    manager = BudgetManager()

    # Основной цикл программы
    while True:
        # Ввод команды пользователя
        command = input("\nВведите команду\n0 - выход, 1 - добавить запись,\n"
                        "2 - редактировать запись, 3 - вывести баланс,\n"
                        "4 - вывести записи, 5 - поиск записей,\n"
                        "6 - записать данные, 7 - загрузить данные: ")

        print('\n')

        match command:

            # Выход из программы
            case '0':
                break

            # Добавление записи
            case '1':
                date = util.enter_date()
                category = util.enter_category()
                amount = util.enter_amount()
                description = input('Введите описание: ')

                record = Record(date, category, amount, description)
                manager.add_record(record)

            # Редактирование записи
            case '2':
                index = int()

                while index not in range(1, len(manager.records) + 1):
                    index = int(input('Введите номер записи для редактирования: '))

                date = util.enter_date()
                category = util.enter_category()
                amount = util.enter_amount()
                description = input('Введите описание: ')

                record = Record(date, category, amount, description)
                manager.edit_record(index - 1, record)

            # Вывод баланса
            case '3':
                print(manager.get_balance())

            # Вывод записей
            case '4':
                print(manager.get_records())

            # Поиск записей
            case '5':
                while True:
                    # Ввод поля для поиска
                    search_field = input('Введите поле для поиска\n'
                                         '1 - Категория (доход/расход), 2 - Дата (гггг-мм-дд)\n'
                                         '3 - Сумма (целое число), 0 - Отмена: ')

                    match search_field:
                        # Поиск по категории
                        case '1':
                            category = util.enter_category()
                            records = manager.search_records(category=category)
                            if records:
                                for record in records:
                                    print(f'\n{record}')
                            else:
                                print("Не найдено записей по вашему запросу")
                            break

                        # Поиск по дате
                        case '2':
                            date = util.enter_date()
                            records = manager.search_records(date=date)
                            if records:
                                for record in records:
                                    print(f'\n{record}')
                            else:
                                print("Не найдено записей по вашему запросу")
                            break

                        # Поиск по сумме
                        case '3':
                            amount = util.enter_amount()
                            records = manager.search_records(amount=amount)
                            if records:
                                for record in records:
                                    print(f'\n{record}')
                            else:
                                print("Не найдено записей по вашему запросу")
                            break

                        # Отмена поиска
                        case '0':
                            break

            # Запись в файл
            case '6':
                manager.save_data()
                print('Данные успешно записаны')

            # Чтение из файла
            case '7':
                try:
                    manager.load_data()
                    print('Данные успешно загружены')
                except FileNotFoundError:
                    print('Файл не найден')
                except ValueError:
                    print('Файл содержит некорректные данные')
                except IndexError:
                    print('Файл содержит некорректные данные')


if __name__ == '__main__':
    main()
