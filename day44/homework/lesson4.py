# 4) Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).
n = int(input("Enter a number: "))
total = 0

for i in range(1, n+1):
    total += i