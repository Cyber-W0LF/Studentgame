import random


class Wallet:
    def __init__(self, stdMoney):
        self.money = stdMoney

    def addMoney(self, money):
        self.money += money

    def __json__(self):
        return {'money': self.money}


class Work:
    def __init__(self, name: str, salary: int, hours):
        self.name = name
        self.salary = salary
        self.hours = hours

    def __str__(self):
        return (f'{self.name}'
                f'\n{self.salary * self.hours}₽'
                f'\n{self.hours}ч.')

    def __json__(self):
        return {'name': self.name, 'salary': self.salary, 'hours': self.hours}

class Vacations:
    cashier = Work('касcир', (random.randint(700, 1500)), 7)
    loader = Work('грузчик', random.randint(500, 900), 6)
    street_cleaner = Work('дворник', random.randint(250, 500), 4)
    volunteer = Work('волонтер', random.randint(800, 1200), 7)
    cleaner = Work('уборщик', random.randint(250, 500), 2)
    consultant = Work('консультант', random.randint(500, 1000), 7)
    courier = Work('курьер', random.randint(550, 2000), 5)
    advertiser = Work('рекламщик', random.randint(600, 700), 3)
    washer = Work('мойщик', random.randrange(500, 1000, 100), random.randint(1, 10))
    waiter = Work('офицант', random.randint(600, 1000), 6)
    works = [cashier, loader, street_cleaner, volunteer, cleaner, consultant, courier, advertiser, washer, waiter]

    @classmethod
    def all(cls ):
        for work in cls.works:
            if work is cls.washer:
                print(f'{work.name}'
                f'\n{work.salary * work.hours}₽'
                f'\n{work.hours} машин')
            else: print(work)



class Student:
    def __init__(self):  # born student
        self.nick = self.__SetNick()
        self.age = random.randint(18, 21)
        self.money = random.randint(4000, 6000)
        self.wallet = Wallet(self.money)
        self.works = random.sample(Vacations.works, k=3)

    def toWork(self, index):
        self.wallet.addMoney(self.works[index].salary)
        print(self.money, 'на счету:'
                          '\n заработано:', self.works[index].salary)

    def __SetNick(self):
        return input('Имя: ')

    def __str__(self) -> str:
        _works = ''
        for work in self.works:
            if  work is Vacations.washer:
                _works += (f'{work.name}\n'
                   f'{work.salary * work.hours} за {work.hours} машин\n')
            else:
                _works += (f'{work.name}\n'
                   f'{work.salary * work.hours} за {work.hours} ч\n')

        return (f'возраст:{self.age}\n'
                f'деньги:{self.wallet.money}₽'
                f'\n{_works}')

    def __json__(self):
        return {
            'nick': self.nick,
            'age': self.age,
            'money': self.money,
            'wallet': self.wallet.__json__(),
            'works': [work.__json__() for work in self.works]
        }