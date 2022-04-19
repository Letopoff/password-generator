import random
alf = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
password = ""
len_password = int(input("Введите длину пароля\n"))
for i in range(len_password):
    password = password + random.choice(alf)
print(password)