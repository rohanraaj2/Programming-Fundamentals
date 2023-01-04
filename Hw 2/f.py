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
    while num1.isdigit() == False:
        print("Input can be a positive integer only. Try Again!")
        num1 = input ()
    num1 = int(num1)
    while num1 == 0:
        print("Input must be greater than 0.")
        num1 = input()
        main (num1)
    num1 = int(num1)
    print ("There are", get_factors(num1), "factors of", num1)


        
if __name__ == "__main__":
    main(num1)
