def bin_sqrt(A):
    """
    Approximates square root of A using binary search
    """
    epsilon = 0.000001
    low = 0.0
    high = A
    guess = 1.0
    while abs(guess**2 - A) >= epsilon:
        if guess**2 < A:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    return guess


print(bin_sqrt(930675566))  # Output: 30506.97569409332
