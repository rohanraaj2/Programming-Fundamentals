def split_dates(s):
    x = s.split()
    l = []
    if len(s) > 0:
        for i in x:
            di = {'year':0, 'month': 0, 'day':0}
            di['year'] = int(i[0:4])
            di['month'] = int(i[5:7])
            di['day'] = int(i[8:10])
            l.append(di)
        return (l)
    

s = input().strip()
from pprint import pprint
pprint(split_dates(s))
