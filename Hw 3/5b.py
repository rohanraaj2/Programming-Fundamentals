# Enter your code here.
n = int(input ())
def generate_ids(n):
    #print (n)
    email = ""
    s = 0
    c = 0
    p = 0
    if n > 0:
        for i in range (n):
            name = input()
            #print (name)
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
                        
            #while email == "":
                #name = input()
            if c == 1:
                f = name.find(" ")
                email += name[f + 1]
            elif c > 1:
                email += name[p]
            
            if s < 10:
                email += "0000" + str(s) + "@st.hu.edu.pk"
            elif s > 9 and s < 100:
                email += "000" + str(s) + "@st.hu.edu.pk"
            elif s > 99 and s < 1000:
                email += "00" + str(s) + "@st.hu.edu.pk"
            elif s > 999 and s < 10000:
                email += "0" + str(s) + "@st.hu.edu.pk"
            else:
                email += str(s) + "@st.hu.edu.pk"
            print (email)
            s += 1
            email = ""

generate_ids(n)
