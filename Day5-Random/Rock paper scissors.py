import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[8,rock,paper,scissors]
print("You are playing ROCK PAPER SCISSORS")
b=int(input("Enter 1 for 'ROCK' 2 for 'PAPER' and 3 for 'SCISSORS"))
c=random.randint(1,3)
if(b==c):
    print("it is a tie")
    print("You chose:")
    print(list[b])
    print("------------------------------------------------------------------")
    print("The computer chose")
    print(list[c])
elif (b==1 and c==2) or (b==2 and c==3) or (b==3 and c==1):
        print("You lose")
        print("You chose:")
        print(list[b])
        print("------------------------------------------------------------------")
        print("The computer chose")
        print(list[c])
elif (b == 1 and c == 3) or (b == 2 and c == 1) or (b == 3 and c == 2):
    print("You Win")
    print("You chose:")
    print(list[b])
    print("------------------------------------------------------------------")
    print("The computer chose")
    print(list[c])