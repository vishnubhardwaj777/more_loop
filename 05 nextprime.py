number = int(input("enter a number -:"))
multiple = number * number

for e in range(number+1,multiple+1):
    if e > 2:
        for i in range(2,e):
            if(e%i == 0):
                break
        else:
            print(e)
            break    


