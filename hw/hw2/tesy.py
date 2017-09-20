def ask_yes_or_no():
    a = int(input("wanna another shot? 1 for yes,0 for no\n"))
    if a == 1:
        print("he choose",a)
        return 1
    elif a == 0:
        print("he choose",a)    
        return 0

#print(ask_yes_or_no())
b=ask_yes_or_no()
print(b)