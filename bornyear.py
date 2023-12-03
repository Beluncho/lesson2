born_year = 1799
print('Ответ вводите цифрами.')
answer = int(input('Введите год рождения Пушкина А.С.: '))

if answer == born_year:
    print('Верно!')
elif answer > born_year:
    print('Неверно. Он родился раньше')
elif answer < born_year:
    print('Неверно. Он родился позднее')

