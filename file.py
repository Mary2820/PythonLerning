# fw = open('doc/file_1.txt', 'a')
# fw.write("Hello Dima\n")
# fw.close()

# fw = open('doc/file_2.txt', 'a')
# fw.write("Hello Kiril\n")
# fw.close()

# a - запись новых данных, и помещение новых данных в конец файла
# w - запись новых данных, но с удалением старых
# r - чтение данных / вывод на консоль

fr = open('doc/file_2.txt', 'r')
text = fr.read()
fr.close()
print(text)


