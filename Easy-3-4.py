rows = int(input("n : "))

i = 1 
while i <= rows :
    k = 1
    while k < i:
        print(' ', end='')
        k += 2
    print('*',end="")
    j = rows 
    while j > i+1:
        print(" ",end='')
        j-=1
    if i == rows and i % 2 != 0:
        print()
    else : 
        print('*') 
    i+=2

i = 2
while i <= rows :
    k = rows
    while k > i + 1 :
        print(' ', end='')
        k -= 2
    print('*',end="")
    j = 1 
    if rows % 2 == 0 :
        while j < i - 1:
            print(" ",end='')
            j+=1
    else:
        while j < i:
            print(" ",end='')
            j+=1
    print('*')
    i+=2

