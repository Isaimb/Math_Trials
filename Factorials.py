from math import factorial

def permutation(n, k):
    return factorial(n)//factorial(n-k)

def combination(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))

n_int = int(input('Enter n value: '))
k_int = int(input('Enter k value: '))

perm = permutation(n_int, k_int)
comb = combination(n_int, k_int)

print(f"\nPermutations (P({n_int}, {k_int})): {permutation(n_int, k_int)}")
print(f"Combinations (C({n_int}, {k_int})): {combination(n_int, k_int)}")
