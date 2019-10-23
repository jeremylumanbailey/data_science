# Google challenge at VCU to calculate number of coins from blocks

sum = 0
for fizzbuzz in range(1001):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:

        sum = (sum + (10 * fizzbuzz))
        continue
    elif fizzbuzz % 3 == 0:

        sum = (sum + (2 * fizzbuzz))
        continue
    elif fizzbuzz % 5 == 0:

        sum = (sum + (3 * fizzbuzz))
        continue
    else:
        sum = (sum + fizzbuzz)
    print(sum)
print(sum)
