import settings
from record import Record


class BudgetManager:
    def __init__(self) -> None:
        self.records = []

    def add_record(self, record: Record) -> None:
        self.records.append(record)

    def edit_record(self, index: int, record: Record) -> None:
        self.records[index] = record

    def get_records(self) -> str:
        result = str()

        if not self.records:
            return 'Записи отсутствуют'

        for i, record in enumerate(self.records):
            result += f'\nЗапись {i+1}\n{str(record)}'

        return result

    def get_balance(self) -> str:
        total_income = sum(record.amount for record in self.records if record.category == 'доход')
        total_expense = sum(record.amount for record in self.records if record.category == 'расход')
        balance = total_income - total_expense

        return f"\nБаланс: {balance}\n" \
               f"Доходы: {total_income}\n" \
               f"Расходы: {total_expense}\n"

    def search_records(self, category: str = None, date: str = None, amount: int = None) -> list:
        result = []
        for record in self.records:
            if record.category == category or record.date == date or record.amount == amount:
                result.append(record)
        return result

    def save_data(self) -> None:
        with open(settings.DATA_FILE, 'w', encoding='utf8') as file:
            for record in self.records:
                file.write(f'{record}\n')

    def load_data(self) -> None:
        records = []
        with open(settings.DATA_FILE, 'r', encoding='utf8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                date = lines[i].strip().split(': ')[1]
                category = lines[i + 1].strip().split(': ')[1]
                amount = int(lines[i + 2].strip().split(': ')[1])
                description = lines[i + 3].strip().split(': ')[1]

                record = Record(date, category, amount, description)
                records.append(record)

            self.records = records
