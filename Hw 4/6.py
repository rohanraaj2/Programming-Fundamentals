def partition_modulo_n(n, t):
    d = {}
    k = []
    if n != 0:
        for i in t:
            if type(i) == int:
                r = i % n
                if r not in d:
                    d[r] = [i]
                else:
                    d[r].append(i)
        if n > 0:
            for j in range(n):
                if j not in d:
                    d[j] = []
        elif n < 0:
            for j in range(n + 1, 1):
                if j not in d:
                    d[j] = []
        return d

from pprint import pprint
n = int(input().strip())
t = [int(i) for i in input().strip().split()]
pprint(partition_modulo_n(n, t))
pprint(t)
