def uniqueelements(lst):
    lst_new=[]
    for i in lst:
        if i not in lst_new:
            lst_new.append(i)
    return lst_new
c=int(input("Enter the number of items you want to enter  in the list : "))
lst=[]
for j in range(c):
    n=eval(input("Enter the item : "))
    lst.append(n)
print("The list is : ",lst)
print("New list of unique elements : ",uniqueelements(lst))
