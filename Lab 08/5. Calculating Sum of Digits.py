n = int(input())
def sum_digits(n):
 a = n % 10
 b = n // 10
 if b == 0:
 return a
 else:
 return (a + (sum_digits(b)))
