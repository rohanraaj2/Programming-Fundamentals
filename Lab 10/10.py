import ast
lst = input()
lst = ast.literal_eval(lst)

def check_types(lst):
    x = []
    #y = []
    if type (lst) != list and "list" not in x:
        return "Error: Bad argument. Function 'check_types' only accept lists"
    else:
        for i in lst:
            if type (i) == str and "str" not in x:
                x.append("str")
            elif type (i) == bool and "bool" not in x:
                x.append("bool")
            elif type (i) == int and "int" not in x:
                x.append("int")
            elif type (i) == float and "float" not in x:
                x.append("float")
            elif type (i) == list:
                if "list" not in x:
                    x.append("list")
                y = check_types(i)
                for j in y:
                    if j not in x:
                        x.append(j)
            
        return (x)

print(check_types(lst))
