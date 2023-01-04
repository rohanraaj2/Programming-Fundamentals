n = int(input())
def breakdown(n):
    a = 0
    b = 0
    c = []
    if n < 100000 and n > -100000:
        while n > 0:
            if n // 10 == 0:
                b = 1
                a = n // b
                for i in range (a):
                    c.append(b)
                n = n // 10
            if n // 100 == 0:
                b = 10
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 1000 == 0:
                b = 100
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 10000 == 0:
                b = 1000
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 100000 == 0:
                b = 10000
                a = n // b
                for i in range (a):
                    c.append(b)
            n = n % b
        
        while n < -1:
            if n // 10 == -1:
                b = -1
                a = n // b
                for i in range (a):
                    c.append(b)
                n = n // 10
            if n // 100 == -1:
                b = -10
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 1000 == -1:
                b = -100
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 10000 == -1:
                b = -1000
                a = n // b
                for i in range (a):
                    c.append(b)
            elif n // 100000 == -1:
                b = -10000
                a = n // b
                for i in range (a):
                    c.append(b)
            n = n % b
                
    
                        
                            
        
        return c
# Enter your code here.
print(breakdown(n))
