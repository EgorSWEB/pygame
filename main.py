file = open('workwithfiles/data.txt', 'w')
# file.write(str(10 + 1))
# print('eeee' + 'gggg') # 'eeeegggg'
# print('eeee' + '\n' + 'gggg') # 'eeee'
#                               'gggg'
# записываем 1000 чисел в файл
for i in range(1000):
    file.write(str(i) + '\n')

file.close()


file = open('workwithfiles/input.txt', 'r')
# s = file.read()
for line in file:
    print('Line:', line)

file.close()