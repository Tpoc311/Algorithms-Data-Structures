# Finding greatest common factor
# Number for test: 4851, 3003 = 231
def nod(a, b):
    # At each step of the cycle, the remainder of dividing a by b is calculated
    # then variable a is assigned the value of variable b
    # variable b is assigned the remainder of dividing a by b
    # the process stops when b = 0
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


print('Enter number a: ')
a = int(input())
print('Enter number b: ')
b = int(input())
out = nod(a, b)
print('Result: ', out)