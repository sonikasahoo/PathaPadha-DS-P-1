#Find greatest number among 3 no.s
num1=float(input("Enter the numbers : "))
num2=float(input())
num3=float(input())
if(num1<num2 and num1<num3):
    if(num2<num3):
        print(num3)
    else:
        print(num2)
if(num2<num1 and num2<num3):
    if(num1<num3):
        print(num3)
    else:
        print(num1)
else:
    if(num1<num2):
        print(num2)
    else:
        print(num1)
