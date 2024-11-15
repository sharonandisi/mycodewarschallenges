import math

def primeFactors(n):
    factors = []  # List to store factors

    # Check divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check divisibility by 3
    while n % 3 == 0:
        factors.append(3)
        n //= 3

    # Check divisibility for potential primes using 6k ± 1 rule
    i = 5
    while i * i <= n:  # Only check up to square root of n
        if n % i == 0:
            factors.append(i)
            n //= i
        elif n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)
        else:
            i += 6  # Skip even numbers and multiples of 3

    # If n is still greater than 1, it must be prime
    if n > 1:
        factors.append(n)

    # Format the result string
    result = ''
    factor_count = {}  # Count occurrences of each factor
    for factor in factors:
        factor_count[factor] = factor_count.get(factor, 0) + 1

    for factor in sorted(factor_count.keys()):  # Sort factors in ascending order
        count = factor_count[factor]
        if count == 1:
            result += f"({factor})"
        else:
            result += f"({factor}**{count})"

    return result


    pass
