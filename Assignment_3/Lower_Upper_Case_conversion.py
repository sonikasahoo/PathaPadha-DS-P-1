string=str(input("Enter a string : "))
print(string)
for i in string:
    if(i.isupper()):
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
