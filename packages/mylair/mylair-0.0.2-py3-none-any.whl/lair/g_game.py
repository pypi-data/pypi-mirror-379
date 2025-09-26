import random
numbers_g = list(range(1, 101))

def g_game():
    cinput = random.choice(numbers_g)

    print('Computer has chosen a number between 1-100 and you have to guess it in 5 tries or less')
    global tries

    while True:
        pinput = int(input('Choose a number: '))

        if pinput not in numbers_g:
            print('is yo ah dum??')

        if pinput > cinput:
            tries -= 1
            print('Lower')
            print(f"{tries} Tries left")

        elif pinput < cinput:
            tries -= 1
            print('Higher')
            print(f"{tries} Tries left")

        else:
            print("You've guessed it right mg")
            break

        if tries == 0:
            print('No mo tries left')

        else:
            continue