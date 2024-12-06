# from functools import cache

# @cache
def recursive_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def recursive_fibonacci_cached(n):
    if n not in c:
        if n <= 1:
            ans = 1
        else:
            ans = recursive_fibonacci_cached(n-1) + recursive_fibonacci_cached(n-2)
        c[n] = ans

    return c[n]


c = {}
n = 350

print(recursive_fibonacci_cached(n))
print(recursive_fibonacci(n))