A = int(input('Введите целое десятичное число: '))
k = 0
if not(A // 10 == 0):
    n = A % 10
    C = n
    B = A
    while True:
        B = B // 10
        m = B % 10
        k = k+1
        C = C + m*(10**k)
        if C == A: break
    if (n % 2 == 0) and (m % 2 == 0):
            if (A > 0):
                A = A-n + m - m*(10**k) + n*(10**k)
            else:
                A = A + n - m + m*(10**k) - n*(10**k)
else:
    print('Введите число больше 10')
print(A)
