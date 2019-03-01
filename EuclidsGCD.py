"""
ALGORITHM Euclid'sGcd(m, n)
Finds the GCD of two numbers using Euclid's GCD Algorithm
Input: 2 integers (m and n)
Output: the GCD of the 2 integers (m and n)
"""


def euclid_gcd(m, n):
    x = m
    y = n
    while n != 0:
        r = m % n
        m = n
        n = r
    print('GCD of ' + str(x) + ' & ' + str(y) + ' is: ' + str(m))


print('\t\n\n========= Euclid\'s GCD Algorithm =========\n\n')
euclid_gcd(int(input('First Number: ')), int(input('Second Number: ')))
