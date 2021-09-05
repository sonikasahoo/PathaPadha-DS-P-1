def palindromeOrNot(s):
    if(len(s)==0):
        print("empty string")
    else:
        s1=s[::-1]
        if(s1==s):
            print("The String is Palindrome")
        else:
            print("The String is not Palindrome")
s=str(input("Enter the string : "))
palindromeOrNot(s)
