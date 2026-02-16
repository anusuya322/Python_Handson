
#1 Dictionary cache inside the function
def fib(n):
    cache = {0: 0, 1: 1}
    def helper(k):
        if k in cache:
            return cache[k]
        cache[k] = helper(k-1) + helper(k-2)
        return cache[k]
    return helper(n)
num = int(input("Enter n: "))
print("Fibonacci number:", fib(num))


#2 Custom @memoize decorator
def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper
@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
num = int(input("Enter n: "))
print("Fibonacci number:", fib(num))
