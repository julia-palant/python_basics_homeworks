'''
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

#print(type(time))
while True:
    time = input('Введите время в секундах: ')
    if time.isdigit():
        time = int(time)
        break
    else:
        print('Введите целое число')

hours = time // 60 // 60
seconds = time % 60
minutes = time // 60 - hours * 60
result = (f"{hours:>02}:{minutes:>02}:{seconds:>02}")
print(result)
