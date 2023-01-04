import ast
my_list = input()
lst = ast.literal_eval(my_list)
def removeDuplicates(lst):
    y = []
    c = 0
    p = 0
    x = 0
    for i in lst:
        c += 1
    for k in lst:
        x = 0
        for j in range (c):
            if lst [j] == k:
                if k not in y:
                    y.append(k)
            
    return y

# Enter your code here. Read input from STDIN. Print output to STDOUT
newList = removeDuplicates(lst)
