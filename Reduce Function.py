from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(Fraction,fracs, 1)
    return t.denominator , t.numerator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
