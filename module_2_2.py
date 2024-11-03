first = input('введите первое число: ')
second = input('введите второе число: ')
third = input('введите третье число: ')
if first == second == third:
    print('количество одинаковых цифр: 3' )
elif first == second or second == third or first == third:
        print('количество одинаковых цифр: 2' )