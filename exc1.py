from math import gcd

def fibonacci_recursive(n: int) -> int:
    # print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(7))


def fibonacci_iter(n: int) -> int:
    a = 0 
    b = 1
    if n < 0:
        raise ValueError("Wrong input.")
    elif n == 0 or n == 1:
        return n
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


print(fibonacci_iter(7))
# numbers = [i for i in range(0,111)]
# print(numbers)
# for i in numbers:
#     print(i, fibonacci(i))

def nwd_recursive(a, b):
    return nwd_recursive(b, a % b) if b else a

def nwd_iter(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

# print(list(map(NWD, numbers)))
print("nwdrec", nwd_recursive(150, 56), "gcd", gcd(150, 56)) 
print("nwditer", nwd_iter(33, 111), "gcd", gcd(33,111)) 


def factorial(n): return n * factorial(n-1) if n > 1 else 1
print("rec", factorial(5))

def factorial_iter(n: int) -> int:
    f = 1
    for i in range(2, n+1):
        # print(f, i)
        f = f*i 
        # print("p", f, i)
    return f
print("iter", factorial_iter(5))

nums = [i for i in range(1,9)]
def sum_list(numbers: list[int]):
    if len(numbers) == 1:
        return numbers[0]
    else:
        print(numbers[0], sum(numbers))
        return numbers[0] + sum_list(numbers[1:])
    
print(sum_list(nums))

nest_nums = [[i for i in range(1,4)] for item in nums]
def recursely_sum_list(data: list[int]) -> int:
    summary = 0

print(nest_nums)