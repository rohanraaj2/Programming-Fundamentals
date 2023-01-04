import ast
A = input()
A = ast.literal_eval(A)
B = input()
B = ast.literal_eval(B)
def matrix_addition(A,B):
    x = []
    y = []
    for i in range (len (A)):
        if len(A[i]) != len(B[i]):
                return ("Matrices A and B don't have the same dimension required for matrix addition.")
        else:
            for j in range (len(A[i])):
                x.append(A[i][j] + B[i][j])
            y.append(x)
            x = []
    
    return y

print(matrix_addition(A,B))
