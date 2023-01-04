import ast
numList = input()
lst = ast.literal_eval(numList)

def odd_items(lst):
    x = []
    for i in lst:
        if i % 2 == 1:
            x.append(i)
    return x
    

# Enter your code here. Read input from STDIN. Print output to STDOUT

my_list = odd_items(lst)
print(my_list)
