month_names = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December' }

def print_dates_in_long_form(t):
    if len(t) > 0:
        for d in t:
            print (month_names[d['month']], str(d['day']) + ",", d['year'])

t = eval(input().strip())
print_dates_in_long_form(t)
