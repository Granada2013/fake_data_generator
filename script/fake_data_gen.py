from mimesis import Generic, locales
from mimesis.enums import Gender
from random import randint, choice
import csv


def generate_user() -> dict:
    """Создание случайного фейкового пользователя"""
    loc = tuple(locales.SUPPORTED_LOCALES.keys())
    gender = {Gender.FEMALE: 'Female', Gender.MALE: 'Male'}
    user = Generic()
    cntry = loc[randint(0, 32)]
    gen = choice(list(gender.keys()))
    res = {'nickname': user.person().username(),
           'first_name': user.person(f'{cntry}').first_name(gen),
           'last_name': user.person(f'{cntry}').last_name(gen),
           'gender': gender[gen],
           'age': user.person().age(minimum=18, maximum=60),
           'country': user.address(f'{cntry}').country(),
           'profile_pic': user.person().avatar()
           }
    return res


def create_csv(path: str, n: int):
    """Создание csv-файла с данными об n фейковых пользователях"""
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file,
                                ['nickname', 'first_name', 'last_name', 'gender', 'age', 'country', 'profile_pic'])
        writer.writeheader()
        for _ in range(n):
            writer.writerow(generate_user())


def selftest():
    create_csv('fake_users.csv', 20)
    with open('fake_users.csv', encoding='utf-8') as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    selftest()
