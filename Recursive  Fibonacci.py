def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
import time

n = 35

# Naive
start = time.time()
print("Naive:", fib_naive(n))
print("Naive Time:", time.time() - start)

# Memoized
start = time.time()
print("Memoized:", fib_memo(n))
print("Memoized Time:", time.time() - start)