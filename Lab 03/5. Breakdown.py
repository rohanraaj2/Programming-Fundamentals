num4 = int(input())
def breakdown(num4):
 print("Thousands:", num4 // 1000)
 new = num4 % 1000
 print("Hundreds:", new // 100)
 new = num4 % 100
 print("Tens:", new // 10)
 new = num4 % 10
 print("Units:", new)

breakdown(num4)
