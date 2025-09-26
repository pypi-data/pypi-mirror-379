import random

def rps():
   list = ['R', 'Rock', 'P', 'Paper', 'S' 'Scissor']
   pinput = None
   cinput = None
   p_score = 0
   c_score = 0

   while True: 

    pinput = input('Choose (Rock, Paper, Scissor) or q to quit: ').strip().capitalize()

    if pinput == "Q":
       break

    if pinput not in list:
       print("Wtf is wrong w you nigga")
       continue
    
    cinput = random.choice(list)

    print(f"Player chose: {pinput}" )
    print(f"Computer chose: {cinput}" )

    if pinput == cinput:
      print("It's a tie")

    elif (pinput == 'Rock' and cinput == "Scissor") or \
         (pinput == 'Paper' and cinput == "Rock") or \
         (pinput == 'Scissor' and cinput == "Paper"):
        print("You win!")
        p_score += 1
    else:
        print("You lose!")
        c_score += 1

    print(f"Your Score: {p_score} - Computer Score: {c_score}")

    if (p_score == 0 and c_score == 3) or \
       (p_score == 1 and c_score == 3) or \
       (p_score == 2 and c_score == 3):
       print('----You Lost!----')
       break

    elif (p_score == 3 and c_score == 0) or \
         (p_score == 3 and c_score == 1) or \
         (p_score == 3 and c_score == 2):
         print('----You Won!!----')
         break

    else:
       continue
