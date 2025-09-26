import random

numbers_f = list(range(1, 11))


def smart_choice(total):
     safe_points = [6, 17, 28, 39]

     for sp in safe_points:
        if total < sp <= total + 10:
            return sp - total 
        
     return random.choice(numbers_f)


def f2f():
     print("Let's play a game, you and i choose a number, whoevers numbers add to 50 loses")

     total = 0

     while True:
        try:
            pinput = int(input('Choose a number between 1-10: '))
        
        except ValueError:
            print('Is you retarded mfer??')
            continue
        
        if pinput not in numbers_f:
            print('f off bruh')
            continue
        
        total += pinput 
        print(f"You chose - {pinput}, total = {total}")

        if total >= 50:
            print("haha loser!!")
            break

        cinput = smart_choice(total)
        total += cinput
        print(f"I chose - {cinput}, total = {total}")

        if total >= 50:
            print('You won by luck, My guy')
            break