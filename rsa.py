import sys
from math import isqrt, gcd

def pollard_rho(n):
    def f(x):
        return (x*x + 1) % n

    x = 2
    y = 2
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    return d

def factorize_rsa(n):
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
            n //= 2
        else:
            factor = pollard_rho(n)
            factors.append(factor)
            n //= factor
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_rsa(number)
            if len(factors) == 2:
                print(f"{number}={'*'.join(map(str, factors))}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    factorize_file(file_path)

