# Переменные
name_employee = 'Pushkin'
second_name_employee = 'Aleksandr'
surname_employee = 'Sergeevich'
position_employee = 'locksmith/Слесарь'
age_employee = 37
born_employee = 1986
productivity_employee = 2.52
rate_per_hour_employee = 198.08
positive_employee = productivity_employee > 1

# Вывод данных
print('Фамилия: ', name_employee)
print('Имя: ', second_name_employee)
print('Отчество: ', surname_employee)
print('Должность: ', position_employee)
print('Возраст: ', age_employee)
print('Год рождения: ', born_employee)
print('Коэфф. Производительности труда: ', productivity_employee)
print('Норма час: ', rate_per_hour_employee)
if positive_employee is True:
    print('Характеристика сотрудника: ', 'Квалифицированный сотрудник')
else:
    print('Характеристика сотрудника: ', ' Не квалифицированный сотрудник')


# Типы данных
print(type(name_employee))
print(type(second_name_employee))
print(type(surname_employee))
print(type(position_employee))
print(type(age_employee))
print(type(born_employee))
print(type(productivity_employee))
print(type(rate_per_hour_employee))
print(type(positive_employee))
