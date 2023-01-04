# Enter your code here. Read input from STDIN. Print output to STDOUT.
prime_up, prime_down, tron_up, tron_down = input().split()
def race (prime_up, prime_down, tron_up, tron_down):
    prime_up = int(prime_up)
    prime_down = int(prime_down)
    tron_up = int(tron_up)
    tron_down = int (tron_down)
    np, nt = 0, 0
    t = 0, + 0
    k = [t]
    if prime_up > 0 and prime_down and tron_up > 0 and tron_down > 0 and prime_up > prime_down and tron_up > tron_down:
            
        while np != 'OUT' and nt != 'OUT':
                np += prime_up
                if np >= 1000:
                    np = 'OUT'
                else:
                    np -= prime_down
                
                nt += tron_up
                if nt >= 1000:
                    nt = 'OUT'
                else:
                    nt -= tron_down
                
                f = (np,) + (nt,)
                k.append(f)
        
        c = k.index(f)
            
        print (k)
        if np == 'OUT' and nt == 'OUT':
            print ("Tie in", c, "turns!")
        elif np == 'OUT':
            print ("Frog Prime wins in", c, "turns!")
        elif nt == 'OUT':
            print ("Frogatron wins in", c, "turns!")
race (prime_up, prime_down, tron_up, tron_down)
