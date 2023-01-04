# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    return (arr[int(n/2)])
if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
