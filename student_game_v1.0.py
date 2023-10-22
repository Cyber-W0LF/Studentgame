
import sys
import msvcrt
import keyboard
from classes import Student, Wallet, Vacations, Work, Json

print('выберете действие: \n'
      '1 - новая игра\n'
      '2 - продолжить\n'
      '3 - выход\n'
      )
player = Student()
match(int(input('выбор:'))):
    case 1:
        player = Student()
        player.nick = player.SetNick()
        print('ваш персонаж\n',player)
        Json.toJson(player)

    case 2:
        player = Json.fromJson()
        player.days +=1
        print('ваш персонаж\n', player)

    case 3:
        sys.exit(0)

# цукенг
while True:
    V = int(input(f'\nДень:{player.days}'
                  '\nвыбор вакансии:'))
    player.wallet.addMoney(player.works[V -1].salary * player.works[V -1].hours)
    print(f'баланс:{player.wallet.money}₽')
    player.days += 1
    player.updateVacs()
    print(player.works[0])
    print(player.works[1])
    print(player.works[2])
    Json.toJson(player)

