number = int(input("enter a number -:"))
lowerval = int(input("enter a lower value -:"))
multiple = lowerval * lowerval
cnt = 0

for e in range(lowerval+1,multiple+1):
    if e > 2:
        for i in range(2,e):
            if(e%i == 0):
                break
        else:
            if(cnt == number):
                break
            else:
                print(e)
                cnt = cnt + 1 
               

