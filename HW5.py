class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        try:
            amount = float(input("Введите сумму для добавления на счет: "))
            if amount > 0:
                self._balance += amount
                print(f"Счет пополнен на {amount}. Новый баланс: {self._balance}")
            else:
                print("Сумма должна быть положительной.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число.")

    def _kill(self):
        self._balance = 0
        print(f"Все деньги на счету были обнулены. Текущий баланс: {self._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Вы выиграли джекпот! Ваш баланс увеличен в 10 раз и теперь составляет: {self._balance}")

    def _merge_balance(self, other_account):
        if isinstance(other_account, Bank):
            self._balance += other_account._balance
            other_account._balance = 0
            print(f"Баланс объединен. Новый баланс: {self._balance}")
        else:
            print("Ошибка: другой счет должен быть экземпляром класса Bank.")

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль невозможно.")
        return Calculator(self.value / other.value)

    def __str__(self):
        return str(self.value)

acc1 = Bank("bakit", 1000)
acc2 = Bank("batyrkhan", 1500)

acc1.moneyX()
acc1._merge_balance(acc2)
acc1._kill()

calc1 = Calculator(10)
calc2 = Calculator(20)

result_add = calc1 + calc2
print(f"Сложение: {result_add}")
result_sub = calc1 - calc2
print(f"Вычитание: {result_sub}")

result_mul = calc1 * calc2
print(f"Умножение: {result_mul}")

result_div = calc1 / calc2
print(f"Деление: {result_div}")
