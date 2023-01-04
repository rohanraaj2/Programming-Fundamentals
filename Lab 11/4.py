import ast
A = input()
A = ast.literal_eval(A)

def print_matrix(A):
    for i in range (len(A)):
        for j in range (len(A[i])):
            print (A[i][j], end = " ")
        print()
            

print_matrix(A)
