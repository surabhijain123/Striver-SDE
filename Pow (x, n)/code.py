def pow(x, n):
    duplicate = n
    if n < 0:
        n = -n
    l = []
    i = 0
    p = n
    while p != 0:
        if p & (1 << i):
            l.append(1 << i)
            p = p & ~(1 << i)
        i += 1
    
    mem = {}
    mem[1] = x
    i = 1
    while  l and i < l[-1]:
        mem[2*i] = mem[i] * mem[i]
        i = 2 * i
    res = 1
    for i in l:
        res *= mem[i]
    if duplicate >= 0:
        return res
    else:
        return 1/res
