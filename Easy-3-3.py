rows = int(input(" n : "))
i = 1
while i <= rows:
    j = rows
    while j > i:
        print(' ',end='')
        j -= 1
    print('*', end='')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end='')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1
