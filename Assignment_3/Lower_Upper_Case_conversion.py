string="Hey! Nice To Meet You."
print(string)
for i in string:
    if(i.isupper()):
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
