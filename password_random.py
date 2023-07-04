import random
def generate_password():
  password_len = random.randint(7, 10)
  password = ''
  for i in range(password_len):
    password += chr(random.randint(33, 126))
  return password
print(generate_password())