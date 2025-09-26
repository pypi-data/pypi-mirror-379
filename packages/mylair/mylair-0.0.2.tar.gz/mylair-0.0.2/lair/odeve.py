import random

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pinput = None
cinput = None
odeve = None
c_score = 0
p_score = 0



def odeve():
     while True:
          odeve = input('Odd or even?: ').strip().capitalize()

          if odeve in ['O', 'Odd'] :
              if odd():
                  return


          elif odeve in ['E', 'Even']:
               if even():
                   return

          else:
               print('Wrong input Mfer')

               
def odd():
     global p_score, c_score
     pinput = int(input('Choose a number between 1 - 10: '))

     if pinput not in number:
         print('You stupid ni**a')
         return 

     cinput = random.choice(number)

     print(f"You chose - {pinput}")
     print(f"computer chose - {cinput}")
     print(f"Sum of the numbers - {pinput + cinput}")

     if (pinput + cinput) % 2 == 0:
      c_score += 1
      print(f"You - {p_score}  {c_score} - Computer")
      print('----You Lost!!----')

     else:
      p_score += 1
      print(f"You - {p_score}  {c_score} - Computer")
      print('----You Won----')


     if p_score == 3:
      print('Player Won')
      return 

     elif c_score == 3:
      print('Comnputer Won')
      return 

def even():
     global p_score, c_score
     pinput = int(input('Choose a number between 1 or 10: '))

     if pinput not in number: 
      print('You stupid ni**er')
      return
          
     cinput = random.choice(number)

     print(f"You chose - {pinput}")
     print(f"Computer chose - {cinput}")
     print(f"Sum of the number - {pinput + cinput}")

     if (pinput + cinput) % 2 == 0:
      p_score += 1
      print('----You won----')
      print(f"You - {p_score}  {c_score} - Computer")
      
     else:
      c_score += 1
      print('----You Lost!!----')
      print(f"You - {p_score}  {c_score} - Computer")


     if p_score == 3:
         print('Player Won')
         return 

     elif c_score == 3:
         print('Computer Won')
         return