lst=[13,7,-104,8,0,-24,89]
sort_lst=[]
low=lst[0]
while lst:
    low=lst[0]
    for i in lst:
        if(i<low):
            low=i
    sort_lst.append(low)
    lst.remove(low)
print("sorted list : ",sort_lst)
