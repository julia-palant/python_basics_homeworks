""""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    number = input('Введите целое число n: ')
    if number.isdigit():
        number = str(number)
        break
    else:
        print('Введите целое число: ')
print(type(number))
# проверка на стр, если не стр, сделать стр
result = int(number)+int(number*3)+int(number*3)
print(result)
