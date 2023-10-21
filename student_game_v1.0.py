import json
import sys
import msvcrt
import keyboard
from classes import Student, Wallet, Vacations, Work


# student = Student()
# print(student)
#
# with open("save.json", "w", encoding="utf-8" ) as file:
#     json.dump(student, file,default=lambda x: x.__json__(), indent=4, ensure_ascii=False)

json_: str = ''
with open("save.json", 'r',  encoding='utf-8') as file:
    json_ = file.read()
student_dict = json.loads(json_)
student = Student()
student.nick = student_dict['nick']
student.age = student_dict['age']
student.money = student_dict['money']
student.wallet.money = student_dict['wallet']['money']
student.works = [Work(**work_dict) for work_dict in student_dict['works']]
print(student)


