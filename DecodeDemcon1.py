def fibonnaciGenerator():
    a = b = 1

    while True:
        yield b
        a, b = b, a + b

ans = 0
fibGen = fibonnaciGenerator()
b = next(fibGen)
while b < 4e6:
    b = next(fibGen)
    if b % 2 == 0:
        ans += b

print(ans)