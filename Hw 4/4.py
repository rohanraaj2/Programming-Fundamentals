#!/bin/python3

import ast
L = input()
L = ast.literal_eval(L)

def nestedList2Dictionary(L):
    d = {}
    k = []
    for i in L:
        for j in range(1, len(i)):
            if i[0] in d:
                d[i[0]].append(i[j])
            else:
                k.append(i[j])
                d[i[0]] = k
                k = []
    return d
    

if __name__ == '__main__':
    print(nestedList2Dictionary(L))
