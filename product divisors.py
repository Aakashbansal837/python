def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
 
N = input()
a = [int(k) for k in input().split()]
dict_factors = {}
for i in a:
    temp_factors = prime_factors(i)
    for t in temp_factors:
        if t not in dict_factors:
            dict_factors[t] = 1
        else:
            dict_factors[t] += 1
 
product = 1
for k in dict_factors:
    product *= (dict_factors[k] + 1)
    product = product%1000000007
# print(dict_factors)
print(product)
