import ast
my_list = input()
lst1 = ast.literal_eval(my_list)
my_list = input()
lst2 = ast.literal_eval(my_list)

def merge_lists(lst1 , lst2):
    a = []
    a = (lst1 + lst2)
    a.sort()
    return (a)


# Enter your code here. Read input from STDIN. Print output to STDOUT
final = merge_lists(lst1 , lst2)
print(final)
