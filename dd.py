import pytest
import tempfile, os
import csv
file = open('books.txt', 'r', encoding='utf-8')
# создаю функцию кокторя принимает параметр file_name
def get_books(file_name):
# заношу в переменную csv обьект
    books = csv.reader(open(file_name))
    # cоздаю переменную count
    count = 0
    # создаю books_array куда будем добовлять книги
    books_array = []
    # делаю цикл
    for i in books:
    # условие, выполняем код если count > 0
        if count > 0:
            # добовляем в масив books_array книгу где
            books_array.append([
            i[0].split('|')[0],
            i[0].split('|')[1],
            i[0].split('|')[2],
            int(i[0].split('|')[3]),
            float(i[0].split('|')[4])
            ])
            # прибвляем к count еденицу
        count = count + 1
        # возвращаю books_array
    print(books_array)

# вывожу функцию get_books() и передаю туда название файла из которого читаю данные
get_books('books.txt')
