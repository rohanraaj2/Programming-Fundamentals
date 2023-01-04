# Enter your code here.
def compute_profit(stock_info):
    x = 0
    for i in stock_info:
        p = i[2] * (i[4] - i[1])
        x += p
    return (round(x))
s = input().strip().split()
s = [(s[i],float(s[i+1]), int(s[i+2]), s[i+3], float(s[i+4])) for i in range(0, len(s), 5)]
print(compute_profit(s))
