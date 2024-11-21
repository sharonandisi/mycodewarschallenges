def is_even(n): 
    # Check if the input 'n' is either an integer or a float
    # If not, immediately return False since we only care about numbers
    # Also ensures floats with a decimal part (like 3.5) are considered uneven
    if not isinstance(n, (int, float)) or n != int(n):
        return False  

    # check if n is divisible by 2 .If divisible, it's even; otherwise, it's odd
    return n % 2 == 0
    pass
