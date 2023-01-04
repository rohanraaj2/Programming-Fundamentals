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
        if prime_up >= 1000:
            np = 'OUT'
        if tron_up >= 1000:
            nt = 'OUT'
            
        if np != 'OUT' and nt == 'OUT':
            np += prime_up - prime_down
            f = (np,) + (nt,)
            k.append(f)
        if nt != 'OUT' and np == 'OUT':
            nt += tron_up - tron_down
            f = (np,) + (nt,)
            k.append(f)
            
        while np != 'OUT' and nt != 'OUT':
                np += prime_up - prime_down
                if np >= 1000:
                    np = 'OUT'
                
                nt += tron_up - tron_down
                if nt >= 1000:
                    nt = 'OUT'
                
                f = (np,) + (nt,)
                k.append(f)
        
        c = k.index(f)
            
        print (k)
        if np == nt:
            print ("Tie in", c, "turns!")
        elif np == 'OUT':
            print ("Frog Prime wins in", c, "turns!")
        elif nt == 'OUT':
            print ("Frogatron wins in", c, "turns!")
race (prime_up, prime_down, tron_up, tron_down)
