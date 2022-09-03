from random import choice
from string import printable


def random_password(length):
    """
    Генерирует случайный пароль заданной длины
    """

    return "".join([choice(printable) for x in range(int(length))])


if __name__ == "__main__":
    amount = int(input("Сколько паролей генерировать: "))
    number = int(input("Длина пароля: "))

    for i in range(1, amount + 1):
        print(f"   Пароль: {i} - {repr(random_password(number))} ")
