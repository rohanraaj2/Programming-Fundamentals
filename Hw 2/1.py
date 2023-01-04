def years_to_graduate(days):
    y = days // 365
    if y > 0:
        n = days - (365 * y)
        m = n // 30
        d = n % 30
        if m > 0:
            print ("The time left to graduation is", y, "years and", m, "months and", d, "days.")
        else:
            print ("The time left to graduation is", y, "years and", d, "days.")
    else:
        m = days // 30
        d = days % 30
        if m > 0:
            print ("The time left to graduation is", m, "months and", d, "days.")
        else:
            print ("The time left to graduation is", d, "days.")

def days_to_graduate(y, m, d):
    print (((y * 365) + (m * 30) + (d)), "days are left to graduation.")
    

func = input().strip()
if func == 'y':
  days = int(input())
  years_to_graduate(days)
else:
  y, m, d = map(int, input().split())
  days_to_graduate(y, m, d)
