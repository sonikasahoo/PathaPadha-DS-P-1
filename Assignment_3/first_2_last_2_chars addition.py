s=str(input("Enter a string : "))
if(len(s)<2):
    print("empty string")
else:
    s_new=s[0:2]+s[-2:]
    print("new string : ",s_new)
