# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი
def listn (a,b):
    a = int(input("enter your number"))
    b = int(input("enter your number"))
    if a % 2 ==0:
        print("რიცხვი ლუწია")
    if b % 2 !=0:
        print("რიცხვი კენტია") 
print(listn(2,3))   