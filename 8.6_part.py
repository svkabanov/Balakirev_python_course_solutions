'''
Имеется фрагмент программы (см. листинг ниже). При его выполнении возникает ошибка FileNotFoundError.
Запишите конструкцию try / except, чтобы отображалось сообщение "File Not Found", если файл не удается открыть.

f = open("abc.txt")
r = f.read(1)
f.close()


'''

try:
    with open("abc.txt") as f:
        r = f.read(1)
        f.close()
except FileNotFoundError:
    print('File Not Found')
except:
    print('Error during working with file')



