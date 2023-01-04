# Enter your code here.
select = int(input())
message = input()
key = int(input())
        
def encode(message, key):
    s = ""
    x = 0
    y = 0
    if key >= 0:
        for i in message:
            if i.isalpha() == True:
                x = ord(i) + key
                if (x > 90  and x < 97) or x > 122:
                    if x > 90  and x < 97:
                        x = x - 90
                    elif x > 122:
                        x = x - 122
                    y = 64 + x
                    s += chr(y)
                else:
                    s += chr(x)
            else:
                s += i
        return(s.upper())
        
def decode(code, key):
    s = ""
    if key >= 0:
        for j in code:
            if j.isalpha() == True:
                x = ord(j) - key
                if (x > 90  and x < 97) or x < 65:
                    if x > 90  and x < 97:
                        x = 97 - x
                    elif x < 65:
                        x = 65 - x
                    y = 91 - x
                    s += chr(y)
                else:
                    s += chr(x)
            else:
                s += j
        return(s.upper())
    
if select == 1:
    print(encode(message, key))
    
elif select == 2:
    print(decode(message, key))
