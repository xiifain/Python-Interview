def is_prime(number):
    if number <2:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True


number = int(input("Input Number: "))

i = 0
print(f'{number} -> ', end="")
while i < number:
    if is_prime(i):
        print(i, end=" ")
    else:
        pass
    i += 1
