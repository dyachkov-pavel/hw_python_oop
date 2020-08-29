import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return self.get_stats()

    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=6)
        return self.get_stats(today, week_ago)

    def get_stats(self, start_date=None, end_date=None):
        if start_date is None:
            start_date = dt.date.today()
        if end_date is None:
            end_date = dt.date.today()
        counter = sum(
            record.amount for record in self.records if
            start_date >= record.date >= end_date
        )
        return counter

    def get_remainder(self):
        remainder = self.limit - self.get_today_stats()
        return remainder


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remained_calories = self.get_remainder()
        if remained_calories > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более '
                    f'{remained_calories} кКал'
                    )
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    currency_info = {'rub': ('руб', 1),
                     'usd': ('USD', USD_RATE),
                     'eur': ('Euro', EURO_RATE)}

    def get_today_cash_remained(self, currency):
        if currency not in self.currency_info:
            return f'Валюта {currency} не определена'
        remained_cash = self.get_remainder()
        if remained_cash == 0:
            return 'Денег нет, держись'
        currency_name, currency_rate = self.currency_info[currency]
        cash_balance = remained_cash/currency_rate
        if remained_cash > 0:
            return ('На сегодня осталось '
                    f'{cash_balance:.2f} {currency_name}'
                    )
        debt = abs(cash_balance)
        return ('Денег нет, держись: '
                f'твой долг - {debt:.2f} {currency_name}'
                )


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment
