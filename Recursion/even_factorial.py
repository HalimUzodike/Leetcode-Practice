# def even_factorial(n):
#     """
#     Iterative
#     """
#
#     if n == 0 or n == 1:
#         return 1
#
#     ans = 1
#     for num in range(2, n + 1):
#         if num % 2 == 0:
#             ans *= num
#     return ans


# Recursive

def even_factorial(n):
    """
    Recursive
    """
    if n == 0 or n == 1:
        return 1

    if n % 2 == 0:
        return n * even_factorial(n - 2)
    else:
        return even_factorial(n - 1)
    

print(even_factorial(7))    # Should be 48