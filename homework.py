import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = float(limit)
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return self.count()

    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=6)
        return self.count(today, week_ago)

    def count(self, start_date=dt.date.today(), end_date=dt.date.today()):
        counter = sum(
            record.amount for record in self.records if
            start_date >= record.date >= end_date
        )
        return counter


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        todays_calories = self.get_today_stats()
        if todays_calories < self.limit:
            remained_calories = int(self.limit - todays_calories)
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более '
                    f'{remained_calories} кКал'
                    )
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    currency_info = {'rub': ['руб', 1],
                     'usd': ['USD', USD_RATE],
                     'eur': ['Euro', EURO_RATE]}

    def get_today_cash_remained(self, currency):
        todays_expenses = float(self.get_today_stats())
        currency_name, currency_rate = self.currency_info[currency]
        if currency not in self.currency_info.keys():
            return 'Валюта не определена'
        else:
            if todays_expenses < self.limit:
                remained_cash = (self.limit - todays_expenses)/currency_rate
                return ('На сегодня осталось '
                        f'{remained_cash:.2f} {currency_name}'
                        )
            elif todays_expenses == self.limit:
                return ('Денег нет, держись')
            else:
                debt = (todays_expenses - self.limit)/currency_rate
                return ('Денег нет, держись: '
                        f'твой долг - {debt:.2f} {currency_name}'
                        )


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment
