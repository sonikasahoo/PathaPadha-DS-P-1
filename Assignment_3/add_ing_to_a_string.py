s=str(input("Enter a string : "))
if (len(s)<3):
    print(s)
else:
    if(s[-3:]=='ing'):
        print(s[:len(s)-3]+'ly')
    else:
        print(s+'ing')
