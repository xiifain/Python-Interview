rows = int(input(" n : "))
i = 1
while i <= rows:
    if i % 2 == 0 :
        pass
    else:
        j = rows
        while j > i:
            if j % 2 == 0 :
                pass
            else :
                print(' ', end='')
            j -= 1
        print('*'* i)
    i += 1

i = 2
while i <= rows:
    k = rows
    if rows == 2 and i % 2 == 0 :
        print('*')
    elif rows != 2 and i % 2 == 0 :
        pass
    else:
        j = 1
        while j < i:
            if j % 2 == 0 :
                pass
            else :
                print(' ', end='')
            j += 1
            k -= 1
        if rows % 2 == 0 :
            print('*' * (k - 1))
        else:
            print('*' * k)
    i += 1

