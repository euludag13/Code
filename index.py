from random import randint

rand = randint(1, 100)

while True:
    number = int(input("Enter a value between 1 and 100 (0 Exit):"))
    if (number == 0):
        print("Game is Finished")
        break
    elif number < rand:
        print("Number is higher.")
        continue
    elif number > rand:
        print("Number lower.")
        continue
    elif number == rand:
        print("İt's correct")
