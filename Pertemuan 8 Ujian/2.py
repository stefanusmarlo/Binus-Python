x = 5
nama = "Stefanus"

y2h
_t
x

y2h = 0
_t = 18
for x in range(5):
    if x % 2 == 1:
        y2h = _t - x
    elif _t > x:
        _t = _t // x
    else:
        y2h = y2h + 1
    print(x, y2h)
