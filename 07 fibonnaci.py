numberTerm = int(input("enter a  number"))
firstNumber  = int(input("enter a first number"))
secondNumber = int(input("enter a second number"))
cnt = 0
print(firstNumber)
print(secondNumber)

for num in range(numberTerm-2):
    if(num != numberTerm):
        record = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = record
        print(record)
        cnt = cnt + 1

