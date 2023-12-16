file = open('workwithfiles/table.txt', 'a+', encoding="utf-8")
file.write("Таблетки|2 р/д, 7 дней|06.12.23\n")
file.seek(0) # переносит каретку для чтения в начало файла
file.write("Таблетки|2 р/д, 8 дней|06.12.23\n")
print(file.readline().split('|'))
print(file.readline().split('|'))
file.close()