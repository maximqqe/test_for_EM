class Record:
    def __init__(self, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category.lower()
        self.amount = amount
        self.description = description

    def __str__(self) -> str:
        return f'Дата: {self.date}\n' \
               f'Категория: {self.category}\n' \
               f'Сумма: {self.amount}\n' \
               f'Описание: {self.description}\n'
