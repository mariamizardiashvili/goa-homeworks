def numbers_product(start, end, step):
    listn= []
    listm = []
    while start <= end:
        listn.append(start)
        start+=step
       
    for i in listn:
        if i % 3 == 0:
            listm.append(i)
    sum = 1
    for i in listm:
        sum*=i
    return sum

print (numbers_product(1,20,1)) 


def math (x,y):
    print (x+y)
    print(x-y)
    print(x*y)
    print(x/y)
math(500200,100)