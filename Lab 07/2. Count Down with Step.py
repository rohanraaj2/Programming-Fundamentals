import inspect
# Complete the 'countDown' function below.
#
# The function accepts following parameters:
# 1. INTEGER lst
# 2. INTEGER fst
# 3. INTEGER stp
#
def countDown(lst, fst, stp):
 for i in range (fst, lst - 1, stp):
 print (i)
lst = int(input())
fst = int(input())
stp = int(input())
countDown(lst, fst, stp)
