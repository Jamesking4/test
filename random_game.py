import random as rnd
Number = rnd.randint(1,101)
attempt = int(input("Сколько нужно попыток?\n"))

while attempt > 0:
    attempt = attempt - 1
    otvet = input("Угадай число от 1 до 100\n")
    if int(otvet) == int(Number):
        print("Ты угадал!")
        break
    if attempt <= 0:
        print("Ты не угадал, я загадал число",Number)
        break
    elif int(Number) > int(otvet):
        print("Не угадал, больше")
    elif int(Number) < int(otvet):
        print("Не угадал, меньше")

    
        


