def fibonacci_recursive(n: int) -> int:
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(11))

# numbers = [i for i in range(0,111)]
# print(numbers)
# for i in numbers:
#     print(i, fibonacci(i))

def nwd_recursive(a, b):
    return nwd_recursive(b, a % b) if b else a

def nwd_iter(a, b):
    while b:
        a, b = b, a % b
    return a


# print(list(map(NWD, numbers)))
print("nwd", nwd_recursive(15, 56)) 


def factorial(n): return n * factorial(n-1) if n > 1 else 1

4 * 3 * 2 
# 4 * 3 = 12
# 12 * 2 = 24

# 4 * 3 = 12
# 12 * 2 = 24
print("rec", factorial(5))

def factorial_iter(n):
    f = 1
    for i in range(2, n+1):
        # print(f, i)
        f = f*i 
        # print("p", f, i)
    return f
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
# print(24 * 6)
# print(factorial(5))
print("iter", factorial_iter(5))