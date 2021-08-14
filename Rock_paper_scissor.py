import random
import time
import sys
## time module is used for dramatic pause

title = '''
█▀▀█ █▀▀█ █▀▀ █░█ 　 █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ 　 █▀▀ █▀▀ ░▀░ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ 
█▄▄▀ █░░█ █░░ █▀▄ 　 █░░█ █▄▄█ █░░█ █▀▀ █▄▄▀ 　 ▀▀█ █░░ ▀█▀ ▀▀█ ▀▀█ █░░█ █▄▄▀ ▀▀█ 
▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░▀ 　 █▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░▀▀ 　 ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀\n'''

print(title)
rock = '''
Rock \n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper \n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors \n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gameImg = [rock,paper,scissors]
userChoice = int(input("Pick a number! \n 0 for Rock \n 1 for Paper \n 2 for Scissors : \n\n"))

if userChoice>=3 or userChoice<0:
    print("Invalid option! Please Enter a number bw 0 and 2")
    input("Press enter to exit")
    sys.exit()

else:
    
    time.sleep(2)
    print(f"\n Your choice is : \n {gameImg[userChoice]}")




    computerChoice = random.randint(0,2)

    print(f"Computer's Choice is..... \n {gameImg[computerChoice]}")

    time.sleep(1)



    if userChoice==0 and computerChoice==2:
        print('''\n
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 　 █ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 　 ▀ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀ 　 ▄''')
        

    elif computerChoice==0 and userChoice==2:
        print('''\n
█░░█ █▀▀█ █░░█ 　 █░░ █▀▀█ █▀▀ ▀▀█▀▀ 　 █ 
█▄▄█ █░░█ █░░█ 　 █░░ █░░█ ▀▀█ ░░█░░ 　 ▀ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░ 　 ▄''')

    elif userChoice > computerChoice:
        print('''\n
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 　 █ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 　 ▀ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀ 　 ▄''')

    elif computerChoice > userChoice :
        print('''\n
█░░█ █▀▀█ █░░█ 　 █░░ █▀▀█ █▀▀ ▀▀█▀▀ 　 █ 
█▄▄█ █░░█ █░░█ 　 █░░ █░░█ ▀▀█ ░░█░░ 　 ▀ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░ 　 ▄''')

    elif computerChoice== userChoice:
        print('''\n
█▀▀▄ █▀▀█ █▀▀█ █░░░█ 
█░░█ █▄▄▀ █▄▄█ █▄█▄█ 
▀▀▀░ ▀░▀▀ ▀░░▀ ░▀░▀░''')

    input("\nPress enter to exit")
    sys.exit()
