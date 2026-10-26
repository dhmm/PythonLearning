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

#   Rock  |  Paper  |  Scissors
weights = [
    ["0", "2", "1"],
    ["1", "0", "2"],
    ["2", "1", "0"]
]
choices = [ ["Rock", rock] , ["Paper", paper], ["Scissors", scissors]]
computer_choice = int(random.randint(0,2))
user_choice = int(input("Enter your choice (0)Rock, (1)Paper, (2)Scissors : "))

if user_choice < 0 or user_choice > 2:
    print("Invalid Choice")
else:
    result = int(weights[computer_choice][user_choice])
    if result == 2:
        print(f"You win! {choices[user_choice][0]} beats {choices[computer_choice][0]}\n"
              f"{choices[user_choice][1]} >>> BEATS >>> {choices[computer_choice][1]}")
    elif result == 1:
        print(f"You lose! {choices[computer_choice][0]} beats {choices[user_choice][0]}\n"
              f"{choices[user_choice][1]} <<< BEATS <<< {choices[computer_choice][1]}")
    else:
        print("Draw")

