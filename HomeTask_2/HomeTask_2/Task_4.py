"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в
слово длинное, выводить только первые 10 букв в слове. """

user_str = input('Введите строку: ')
arr_str = user_str.split()
for i in range(len(arr_str)):
    print(i, end=' : ')
    if len(arr_str[i]) < 10:
        print(arr_str[i])
    else:
        print(arr_str[i][0:9])
