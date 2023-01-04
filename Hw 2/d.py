num1 = input()

def get_factors(n):
    f = 0
    for i in range (1, n):
        if n % i == 0:
            print (i, end = ", ")
            f += 1
    print (n)
    return (f + 1)

def main(num1):
    x = alpha (num1)
    #y = check_decimal(x)
    #d = int(y)
    #z = check_int(d)
    print ("There are", get_factors(z), "factors of", z)

def alpha(a):
    if a.isalpha() == True:
        print("Input can be a positive integer only. Try Again!")
        a = input()
    check_decimal(a)
    
def check_decimal(b):
    for i in b:
        if i == ".":
            print("Input can be a positive integer only. Try Again!")
            b = input()
            alpha(b)
            break
    b = int(b)
    check_int(b)
            
def check_int(c):
    if c < 0:
        print("Input can be a positive integer only. Try Again!")
        c = input()
        alpha(c)
        
    elif c == 0:
        print("Input must be greater than 0.")
        c = input()
        alpha(c)
    
    else:
        return c
        
if __name__ == "__main__":
    main(num1)
