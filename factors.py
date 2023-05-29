import sys
from math import isqrt

def factorize(n):
    factors = []
    for i in range(2, isqrt(n) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            if len(factors) > 1:
                print(f"{number}={'*'.join(map(str, factors))}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    factorize_file(file_path)

