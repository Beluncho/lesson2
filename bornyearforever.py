born_year = 1799
answer = ''

print('Введите ответ цифрами')

while not answer.isdigit():
    answer = input('Введите год рождения Пушкина А.С.: ')
    if not answer.isdigit():
        print('Введите ответ цифрами')

answer = int(answer)
if answer == born_year:
        print('Верно!!!')
while not answer == born_year:
    answer = int(input('Введите год рождения Пушкина А.С.: '))

    if answer == born_year:
        print('Верно!!!')
    elif answer > born_year:
        print('Он родился раньше')
    elif answer < born_year:
        print('Он родился позжe')
    else:
        print('Введите ответ цифрами')
answer = int(answer)
print('Дата рождения Пушкина А.С. : ', '06.06.1799')
