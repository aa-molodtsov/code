filename = input()
try:
  with open(filename, 'r') as file:
    new_content = ""
    for line in file:
      index = line.find('#')
# Если символ найден, обрезаем строку до этого символа
      if index != -1:
        line = line[:index] + "\n"
# Добавляем обработанную строку к новому содержимому файла
      new_content += line
print(new_content)

except FileNotFoundError:
  print("Файл не найден")
except Exception:
  print("Неизвестная ошибка")