def terbesar(a, b, c):
    return max(a, b, c)

print(terbesar(3, 8, 4))   

def terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
