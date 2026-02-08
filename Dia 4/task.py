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



game_image = [rock, paper, scissors]

#User
choice = int(input("Choose:\n0 - rock\n1 - paper\n2 - scissors\n"))

if choice <0 or choice >2:
    print("Invalid choice")
    exit()

print(game_image[choice])

computer_choice = random.randint(0,2)
print("Computer chose:\n" + game_image[computer_choice])

if game_image[computer_choice] == game_image[choice]:
    print("Draw")
else:
    if (game_image[choice] == 0 and game_image[computer_choice] == 2) or (game_image[choice] == 1 and game_image[computer_choice] == 0) or (game_image[choice] == 2 and game_image[computer_choice] == 1):
        print("You Won!")
    else:
        print("You Lose! x.x")

