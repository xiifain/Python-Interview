position = int(input("n : "))

# + -> ascii 43
# A -> ascii 65
# B -> ascii 66
# C -> ascii 67
# D -> ascii 68
# E -> ascii 69

ascii_num = 65 

# the row count relates to n + (n-1) formula 

rows = position + (position - 1)

# n -> 4 means + is at 4th postion AAA"+"BBB

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
                print(chr(ascii_num), end='')
            j -= 1
        if i == 1:
            print('+', end="")
        else:
            print('+' + chr(ascii_num+4)*(i-2)+ '+', end="")
        k = rows
        while k > i:
            if k % 2 == 0 :
                pass
            else :
                print(chr(ascii_num+1), end='')
            k -= 1
        print()
    i += 1

i = 3
while i <= rows:
    if i % 2 == 0 :
        pass
    else:
        j = 1
        while j < i:
            if j % 2 == 0 :
                pass
            else :
                print(chr(ascii_num+2), end='')
            j += 1
        m = rows - 1
        if i == rows:
            print('+', end="")
        else:
            print('+' + chr(ascii_num+4) * (m - i)+ '+', end="")
            m-=1
        k = 1
        while k < i:
            if k % 2 == 0 :
                pass
            else :
                print(chr(ascii_num+3), end='')
            k += 1
        print()
    i += 1





