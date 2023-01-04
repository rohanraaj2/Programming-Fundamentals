def isValidPassword(password):
    f = length (password)
    if type(f) == str:
        g = lower_case(f)
        if type(g) == str:
            h = upper_case(g)
            if type(h) == str:
                m = numerical (h)
                if type(m) == str:
                    space(m)
        
def length (a):
    if len(a) > 7 and len(a) < 31:
        return(a)
    else:
        print("The password must be between 8 and 30 characters long.")
        
def lower_case(b):
    for i in b:
        if i.islower() == True:
            return(b)
    print("The password must contain a lower case letter.")
            
def upper_case(c):
    for j in c:
        if j.isupper() == True:
            return (c)
    print("The password must contain an upper case letter.")
    
def numerical (d):
    for k in d:
        if k.isdigit() == True:
            return (d)
    print("The password must contain a numeral.")
    
def space(e):
    p = 0
    for l in e:
        if l == " ":
            print("The password must not contain a space character.")
            p +=1
            break
    if p == 0: 
        print("ACCEPTED.")
password = str(input())
