def sum_digits(n):
    if type (n) != int:
        print("Error: bad argument. sum_digits is defined for positive integers only.")
    else:
        y = n
        s = 0
        while y > 9:
            x = y % 10
            y = y // 10
            s += x
        s += y
        while s > 9:
            y = s
            s = 0
            while y > 9:
                x = y % 10
                y = y // 10
                s += x
            s += y
        return s

a = eval(input())
answer = sum_digits(a)
if answer:
    print(answer)
