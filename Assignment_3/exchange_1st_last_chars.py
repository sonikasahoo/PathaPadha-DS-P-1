#method=1
s=str(input("Enter a string : "))
new_string=s[-1:]+s[1:-1]+s[:1]
print(new_string)

#method-2
s=str(input("Enter a string : "))
first=s[:1]
last=s[-1:]
new_string=last+s.lstrip(first).rstrip(last)+first
print(new_string)
