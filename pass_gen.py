import random #pip install random
lower = "qwertyuiopasdfghjklzxcvbnm" #маленькие буквы в пароле
upper = "QWERTYUIOPASDFGHJKLZXCVBNM" #большие буквы в пароле
NUMBER = "0123456789" # цифры
Symbol = "[]{}#()*;._-" # символы

all=lower+upper+NUMBER+Symbol #из чего будет состоять пароль
lenght = 15 #длина пароля. можно поставить свое число, какое захотите
password = "".join(random.sample(all, lenght)) #переменная password. и из чего он будет состоять
print("pswrd :", password) #вывод сообщения с паролем в терминал
