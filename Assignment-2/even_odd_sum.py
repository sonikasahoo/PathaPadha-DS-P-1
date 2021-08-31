sum_even=0
sum_odd=0
for i in range(20,31):
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i
print("Sum of even numbers is : ",sum_even)
print("Sum of odd numbers is : ",sum_odd)
