from distutils.command.build_scripts import first_line_re


num = int(input("enter a number -:"))
reverse = 0
while(num !=0):
    lstdigit = num%10
    reverse = reverse * 10 + lstdigit
    num = num//10
print(reverse)    