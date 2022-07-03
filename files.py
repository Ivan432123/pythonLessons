# var = input('Напиши что-нибудь:')
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# моды
# a - запись новых данных в файл и помещение новых данных в конец файла
# w - запись новых данных, но с удалением старых данных
# r - чтение данных из файла

# fr = open('doc/file2.txt', 'w')
# fr.write("Privet")
# fw.close()
#
# fr = open('doc/file.txt', 'r')
# text = fr.read()
# fr.close()
# print(text)


var = input('Пиши код: ')
fw = open('doc/rts.txt', 'a')
fw.write(var)
fw.close()

fr = open('doc/rts.txt', 'r')
text = fr.read()
fr.close()
print(text)
