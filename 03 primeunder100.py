upperval = int(input("enter a upper value -:"))

for number in range(upperval+1):
    if number > 1:
        for e in range(2,number):
            if(number%e) == 0:
                break
        else:
            print(number)
print()