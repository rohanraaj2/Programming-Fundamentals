lst1 = input().strip().split()
lst2 = input().strip().split()
def common(lst1, lst2):
    x = []
    for i in lst1:
        for j in lst2:
            if (i == j) and (j not in x):
                x.append(j)
    return x
# Enter your code here.
print(common(lst1, lst2))
