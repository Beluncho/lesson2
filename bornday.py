born_year = 1799
print('Ответ вводите цифрами.')
answer = int(input('Введите год рождения Пушкина А.С.: '))

if answer == born_year:
    print('Верно!')
    birth_day = 06.06
    answer2 = input('Введите (дд.мм) день и месяц рождения Пушкина А.С.: ')
    answer2 = float(answer2)
    if answer2 ==  birth_day:
        print('Верно')
    if answer2 != birth_day:
        print('Неверный день рождения')
elif answer > born_year:
    print('Неверно. Он родился раньше')
elif answer < born_year:
    print('Неверно. Он родился позднее')

print('Дата рождения Пушкина А.С. : ', '06.06.1799')
