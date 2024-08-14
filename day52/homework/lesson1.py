import random


choices = ['ქვა', 'ქაღალდი', 'მაკრატელი']

user_choice = input("აირჩიეთ: ქვა, ქაღალდი, მაკრატელი: ")


computer_choice = random.choice(choices)
print(f"კომპიუტერმა აირჩია: {computer_choice}")

if user_choice == computer_choice:
    print("ფრეა!")
elif (user_choice == 'ქვა' and computer_choice == 'მაკრატელი') or \
     (user_choice == 'ქაღალდი' and computer_choice == 'ქვა') or \
     (user_choice == 'მაკრატელი' and computer_choice == 'ქაღალდი'):
    print("თქვენ მოიგეთ!")
else:
    print("კომპიუტერმა მოიგო!")
