import random
lower = "qwertyuiopasdfghjklzxcvbnm" 
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-"

all=lower+upper+NUMBER+Symbol
lenght = 15
password = "".join(random.sample(all, lenght))
print("Sosi hui i ne psihui :", password)