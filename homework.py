import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = float(limit)
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return self.records

    def get_today_stats(self):
        todays_stats = 0
        for record in self.records:
            if record.date == dt.date.today():
                todays_stats += record.amount
        return todays_stats

    def get_week_stats(self):
        week_count = 0
        week_ago = dt.datetime.today().date() - dt.timedelta(days=6)
        for record in self.records:
            if dt.datetime.today().date() >= record.date >= week_ago:
                week_count += record.amount 
        return week_count

class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, record):
        super().add_record(record)

    def get_today_stats(self):
        super().get_today_stats()

    def get_calories_remained(self):
        todays_calories = 0
        for record in self.records:
            if record.date == dt.date.today():
                todays_calories += record.amount
        if todays_calories < self.limit:
            remained_calories = int(self.limit - todays_calories)
            print (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained_calories} кКал')
        else:
            print ('Хватит есть!')

    def get_week_stats(self):
        super().get_week_stats()

class CashCalculator(Calculator):
    USD_RATE = float(73)
    EURO_RATE = float(87)

    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, record):
        super().add_record(record)

    def get_today_stats(self):
        super().get_today_stats()

    def get_today_cash_remained(self, currency):
        todays_expenses = float(0)
        for record in self.records:
            if record.date == dt.date.today():
                todays_expenses += record.amount
        if currency == 'rub':
            if todays_expenses < self.limit:
                remained_cash = round(self.limit - todays_expenses, 2)
                print (f'На сегодня осталось {remained_cash} руб')
            elif todays_expenses == self.limit:
                print ('Денег нет, держись')
            else:
                debt = round(todays_expenses - self.limit, 2)
                print (f'Денег нет, держись: твой долг - {debt} руб')
        elif currency == 'usd':
            if todays_expenses < self.limit:
                remained_cash = round((self.limit - todays_expenses)/self.USD_RATE, 2)
                print (f'На сегодня осталось {remained_cash} USD')
            elif todays_expenses == self.limit:
                print ('Денег нет, держись')
            else:
                debt = round((todays_expenses - self.limit)/self.USD_RATE, 2)
                print (f'Денег нет, держись: твой долг - {debt} USD')
        else:
            if todays_expenses < self.limit:
                remained_cash = round((self.limit - todays_expenses)/self.EURO_RATE, 2)
                print (f'На сегодня осталось {remained_cash} Euro')
            elif todays_expenses == self.limit:
                print ('Денег нет, держись')
            else:
                debt = round((todays_expenses - self.limit)/self.EURO_RATE, 2)
                print (f'Денег нет, держись: твой долг - {debt} Euro')

    def get_week_stats(self):
        super().get_week_stats()

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        if date == None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment



