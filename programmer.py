class Programmer:
  name = "Пётр Иванов"
  position = "Junior"
  worked_hours = 0
  salary_per_hour = 20

s = input()
words = s.split()
for word in words:
  if hasattr(Programmer, word.lower()):
    print(word + " - YES")
  else:
    print(word + " - NO")