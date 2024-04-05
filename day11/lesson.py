import time
num = 10
while num > 0:
    print(num)
    time.sleep(1)
    num -= 1
print("Time is up!")


total = 0
num = int(input("Enter a number (enter 0 to stop): "))
while num != 0:
   total += num
   num = int(input("Enter a number (enter 0 to stop): "))
print("Sum of numbers:"), total


password = "12345678"
while True:
   user_input = input("enter the password: ")
   if user_input == password:
      print("password correct.")
   break
else:
   print("the password is incorrect. Try again.")