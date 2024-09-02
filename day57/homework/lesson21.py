# შექმენით სკრიპტი, რომელიც გამოიმუშავებს შემთხვევით რიცხვს.
name = input("Enter your name: ")#Ask for name
age = int(input("Enter your age: "))#Ask for age, convert to int

print(f"Name: {name}, Age: {age}")#Show name and age

#4
global_var = "I'm global"#Global variable

def local_var_example():
    local_var = "I'm local"#Local variable
    print(global_var)#Print global var
    print(local_var)#Print local var

local_var_example()