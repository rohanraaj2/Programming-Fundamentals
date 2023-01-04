def check_num(x):
    
    if type (x) == str:
        if x.isalpha() == True:
            print("Input can be a positive integer only. Try Again!")
            x = input()
        
        for i in x:
            if i == ".":
                print("Input can be a positive integer only. Try Again!")
                x = input()
                check_num(x)
                break
                
        x = int(x)
        
    if x < 0:
        print("Input can be a positive integer only. Try Again!")
        x = input()
        check_num(x)
        
    elif x == 0:
        print("Input must be greater than 0.")
        x = input()
        check_num(x)
        
    else:
        return x
