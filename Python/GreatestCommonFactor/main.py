# Finding greatest common factor
# Number for test: 4851, 3003 = 231


def greatest_common_factor(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


print('Enter number a: ')
a = int(input())
print('Enter number b: ')
b = int(input())
out = greatest_common_factor(a, b)
print('Result: ', out)
