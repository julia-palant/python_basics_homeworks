"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
while True:
    revenue = input("выручка (рубл.):")
    costs = input("издержки (рубл.):")
    if revenue.isdigit() and costs.isdigit():
        revenue = int(revenue)
        costs = int(costs)
        break
    else:
        print('Введите целое число')
profit = revenue - costs
if profit < 0:
    print("Фирма убыточна, нужно что-то менять")
else:
    while True:
        employees = input("количество сотрудников: ")
        if employees.isdigit():
            employees = int(employees)
            break
        else:
             print('Введите целое число')
    profit_per_epml = profit / employees
    print(f"Выручка на одного сотрудника составит {profit_per_epml} рублей")