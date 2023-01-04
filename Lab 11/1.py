def reverse_slice(t, start, stop):
    l1 = []
    l2 = []
    l3 = []
    if stop != 0:
        l1 = t[0:start]
        l2 = t[start: stop]
        l2.reverse()
        l3 = t[stop: len(t)]
        t[:] = l1 + l2 + l3
    

if __name__ == '__main__':
    t = eval(input())
    start = int(input())
    stop = int(input())
    print(reverse_slice(t, start, stop))
    print(t)
