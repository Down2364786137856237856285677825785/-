import json
import os
from time import sleep


download_folger = os.path.join(os.path.expanduser("~"), "Downloads")

file_path_json = os.path.join(download_folger, 'piggy_data.json')

# Дефолтные данные для JSON файла при создании
basic_data_json = {
    "name": None,
    "balance": 0,
    "currency": None,
    "sum": 0
}


def balance_check(s, b):
    if s > b:
        raise InsufficientFundsError("Недостаточно средств.")

    else:
        pass


class InsufficientFundsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Piggy_bank:

    def __init__(self):
        self.all = self.opening_files()
        self.currencies = {
            1: "₽",
            2: "$",
            3: "€",
            4: "₴"
        }

    # Чтение данных из JSON

    def opening_files(self):

        while True:
            try:
                with open(file_path_json, 'r', encoding='utf-8') as file:
                    json_read = json.load(file)
                    break
            except (FileNotFoundError, json.JSONDecodeError):
                with open(file_path_json, 'w', encoding='utf-8') as file:
                    json.dump(basic_data_json, file,
                              ensure_ascii=False, indent=4)
                    continue

        return json_read

    # Создание копилки
    def creating_piggy_bank(self):

        while True:
            try:
                name = input("Введите название копилки: ")
                amount = float(
                    input("Введите сумму копилки: "))
                print("1. ₽\n2. $\n3. €\n4. ₴")
                currency = int(
                    input("Выберите валюту копилки: "))
            except ValueError:
                print("Неверный ввод!")
                sleep(1)
                continue

            print(
                f"\n{name}\nСумма: {amount}\nВалюта: {self.currencies[currency]}")
            confirm = input("Правильно? да\нет: ").lower()

            if confirm == "да":
                self.all["name"] = name
                self.all["sum"] = amount
                self.all["currency"] = self.currencies[currency]

                with open(file_path_json, 'w', encoding='utf-8') as file:
                    json.dump(self.all, file, ensure_ascii=False, indent=4)
                    break
            else:
                continue

    # Пополнение копилки

    def deposit(self):

        while True:
            try:
                sum = float(
                    input("Введите сумму пополнения: "))
            except ValueError:
                print("Неверный ввод")
                sleep(1)
                continue

            confirm = input(
                f"Вы подтверждаете пополнение {sum}{self.all["currency"]}? да\нет: ").lower()

            if confirm == 'да':
                self.all["balance"] += sum

                with open(file_path_json, 'w', encoding='utf-8') as file:
                    json.dump(self.all, file, ensure_ascii=False, indent=4)
                    print("Копилка успешно пополнена")
                    sleep(1)
                    break
            else:
                break

    # Снятия средсв с копилки
    def withdraw(self):

        while True:
            try:
                amount = float(
                    input("Введите сумму: "))
                balance_check(amount, self.all["balance"])
            except ValueError:
                print("Неверный ввод!")
                sleep(1)
                continue

            except InsufficientFundsError as error:
                print(error)
                sleep(1)
                continue

            confirm = input(
                f"Вы подтверждаете снятия {amount}{self.all["currency"]}? да\нет: ").lower()

            if confirm == 'да':
                self.all["balance"] -= amount

                with open(file_path_json, 'w', encoding='utf-8') as file:
                    json.dump(self.all, file, ensure_ascii=False, indent=4)
                    print("Средства были успешно сняты.")
                    sleep(1)
                    break

            else:
                break

    # Редактирование копилки
    def edit_piggy_bank(self):

        # Редактирование названия
        def name_edit():
            new_name = input("Введите новое название: ")
            confirm = input(
                f"Вы действительно хотите поменять название на {new_name}? да\нет: ").lower()

            if confirm == 'да':
                self.all['name'] = new_name
                with open(file_path_json, 'w', encoding='utf-8') as file:
                    json.dump(self.all, file, ensure_ascii=False, indent=4)
                    print("Название было изменено успешно")
            else:
                pass

        # Редактированяи валюты
        def currency_edit():

            while True:
                print("1. ₽\n2. $\n3. €\n4. ₴")
                try:
                    choice_currency = int(
                        input("Выберите валюту: "))
                except ValueError:
                    print("Неверный ввод!")
                    sleep(1)
                    continue

                confirm = input(
                    f"Вы действительно хотите поменят валюту на {self.currencies[choice_currency]}? да\нет ").lower()

                if confirm == 'да':
                    self.all["currency"] = self.currencies[choice_currency]

                    with open(file_path_json, 'w', encoding='utf-8') as file:
                        json.dump(self.all, file, ensure_ascii=False, indent=4)
                        print("Валюта была успешно изменена.")
                        sleep(1)
                        break
                else:
                    pass

        # Редактирование суммы
        def sum_edit():

            while True:
                try:
                    new_sum = float(
                        input("Введите новую сумму: "))
                except ValueError:
                    print("Неверынй ввод!")
                    sleep(1)
                    continue

                confirm = input(
                    f"Вы действительо хотите поменять сумму на {new_sum}{self.all["currency"]}? да\нет: ").lower()

                if confirm == 'да':
                    self.all["sum"] = new_sum

                    with open(file_path_json, 'w', encoding='utf-8') as file:
                        json.dump(self.all, file, ensure_ascii=False, indent=4)
                        print("Сумма была успешно изменена.")
                        sleep(1)
                        break

        while True:
            print("1. Название\n2. Валюта \n3. Сумма\n\n4. Выход")
            while True:
                try:
                    edit_choice = int(
                        input("Выберите что хотите отредактировать: "))
                except ValueError:
                    print("Неверынй ввод!")
                    sleep(1)
                    continue

                if edit_choice == 1:
                    name_edit()
                elif edit_choice == 2:
                    currency_edit()
                elif edit_choice == 3:
                    sum_edit()
                elif edit_choice == 4:
                    exit = True
                    break
                else:
                    print("Неверный вариант")
                    sleep(1)

            if exit:
                break

    # Обнуление копилки

    def reset_amount(self):
        confirm = input(
            "Вы дейтвительно хотите обнулить копилку? да\нет: ").lower()

        if confirm == 'да':
            self.all["balance"] = 0

            with open(file_path_json, 'w', encoding='utf-8') as file:
                json.dump(self.all, file, ensure_ascii=False, indent=4)
                print("Копилка успешно обнулена.")
                sleep(1)
        else:
            pass

    # ОСТАЛЬНЫЕ МЕТОДЫ

    # Чекает если на балике накопилась нужная сумма
    def check_balance(self):
        while True:
            if self.all["balance"] >= self.all["sum"]:
                print("\nПоздравляю, вы накопили достаточнюу сумму")
                print(
                    "1. Обнулить копилку\n2. Создать новую копилку\n\n3. Оставить все как есть")
                try:
                    confirm = int(
                        input("Хотите обнулить копилку или создать новую?: "))
                except ValueError:
                    print("Неверный ввод")
                    sleep(1)
                    continue

                if confirm == 1:
                    self.reset_amount()
                elif confirm == 2:
                    self.creating_piggy_bank()
                else:
                    pass
            break

    # Чекает если в JSON-е иям и валюта является None чтобы создать копилку

    def data_check(self):
        if self.all["currency"] is None:
            self.creating_piggy_bank()
        elif self.all["name"] is None:
            self.creating_piggy_bank()
        else:
            pass


# Главное меню
def main():

    while True:
        Piggy.check_balance()
        Piggy.opening_files()
        print(f"\n\n{Piggy.all["name"]}")
        print(
            f"Баланс: {Piggy.all["balance"]}{Piggy.all["currency"]}\\{Piggy.all["sum"]}{Piggy.all["currency"]}")
        print("1. Пополнить\n2. Снять\n3. Обнулить\n4. Редактировать\n\n5. Выход")
        try:
            choice = int(
                input("Выберите действие: "))
        except ValueError:
            print("Неверный ввод")
            sleep(1)
            continue

        if choice == 1:
            Piggy.deposit()
        elif choice == 2:
            Piggy.withdraw()
        elif choice == 3:
            Piggy.reset_amount()
        elif choice == 4:
            Piggy.edit_piggy_bank()
        elif choice == 5:
            exit()


Piggy = Piggy_bank()
Piggy.data_check()
main()
