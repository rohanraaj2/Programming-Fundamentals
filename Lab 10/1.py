a=int(input())
b=int(input())

def seven_or_five(a,b):
    lst = []
    for i in range(a, b+1):
        if i % 7 == 0 and i % 5 != 0:
            lst.append(i)
    return lst
# Enter your code here. Read input from STDIN. Print output to STDOUT

my_list = seven_or_five(a,b)
print(my_list)
