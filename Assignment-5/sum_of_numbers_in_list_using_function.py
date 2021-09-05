def sum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
c=int(input("Enter the number of items you want to enter  in the list : "))
lst=[]
for j in range(c):
    n=int(input("Enter the item : "))
    lst.append(n)
print("The list is : ",lst)
print("Sum of all numbers in the list : ",sum(lst))
