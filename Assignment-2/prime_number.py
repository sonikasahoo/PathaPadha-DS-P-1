#Prime number or, not
num=int(input("Enter the number : "))
for i in range(2,8):
    if(num%i==0):
        print(num,"number is not a prime number")
        break
    else:
        print(num,"number is a prime number")
        break
