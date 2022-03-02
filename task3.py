n = int(input('Enter the number '))


def first_function(n):
    summa_n = 0
    while n > 0:
        summa_n += n % 10
        n //= 10
    print('Summa of digits is ', summa_n)
    return summa_n


summa = first_function(n)


def second_function(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print('Amount of digits is ', count)
    return count


dif = second_function(n)

answer = summa - dif
print('Difference of summa and amount is ', answer)


