number = int(input("enter a number -:"))
cnt = 0
for e in range(number):
    if(e != 0):
        if(number%e == 0):
            cnt = cnt + 1
        
if(cnt == 1):
    print("prime number")   
else:
    print("not prime")      
print()      
