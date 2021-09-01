#Prime number or, not
num=int(input("Enter the number : "))
count=0
for i in range(2,8):
    if(num%i==0):
        print(num,"number is not a prime number")
        break
    else:
        count+=1
while(count==6):
    print(num,"number is a prime number")
    break
