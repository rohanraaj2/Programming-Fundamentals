# Enter your code here.
n = int(input ())
def generate_ids(n):
    email = ""
    c = 0
    if n > 0:
        for i in range (n):
            email = ""
            name = input()
            name = name.lower()
            for k in range (len(name)):
                if name[k].isalpha() == True:
                    email += name[k]
                    break
            for j in range (len(name)):
                if name[j] == " ":
                    for y in range (j, len(name)):
                        if name[y].isalpha() == True:
                            c += 1
                            p = j + 1
                            break
                        
            f = name.find(" ")
            s = str(i)
            l = 5 - len(s)
            
            if c == 1:
                email = name [k] + name[f + 1] + ("0" * l) + s + "@st.hu.edu.pk"
            else:
                email = name [k] + name[p] + ("0" * l) + s + "@st.hu.edu.pk"
            print (email)

generate_ids(n)
