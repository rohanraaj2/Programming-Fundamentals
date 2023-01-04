import ast
my_list = input()
lst = ast.literal_eval(my_list)

def first_and_last(lst):
    x = []
    c = 0
    x.append(lst[c])
    for i in lst:
        c += 1
    x.append(lst[c - 1])
    return x

# Enter your code here. Read input from STDIN. Print output to STDOUT

print(first_and_last(lst))
