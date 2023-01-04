def my_bill(all_charges, tab_id):
    l = []
    if type (all_charges) == list and type(tab_id) == int:
        for u in all_charges:
            if len (u) >= 1 and type(u[0]) == int:
                if u[0] == tab_id:
                    s = 0
                    for i in range(1, len(u)):
                        if type(u[i]) == float:
                            s += u[i]
                    l.append(s)
        return l

tab_id = int(input())
all_charges = eval(input())
print(my_bill(all_charges, tab_id))
print(all_charges)
