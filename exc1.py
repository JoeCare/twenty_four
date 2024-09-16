from math import gcd

def fibonacci_recursive(ind: int) -> int:
    # print(n)
    if ind == 0:
        return 0
    elif ind == 1:
        return 1
    else:
        return fibonacci_recursive(ind - 1) + fibonacci_recursive(ind - 2)
print("fibr", fibonacci_recursive(7))
for i in range(20):
    print(i, fibonacci_recursive(i))


def fibonacci_iter(ind: int) -> int:
    a = 0 
    b = 1
    if ind < 0:
        raise ValueError("Wrong input.")
    elif ind == 0 or ind == 1:
        return ind
    else:
        for i in range(2, ind + 1):
            c = a + b
            a = b
            b = c
        return c

print(fibonacci_iter(7))

def fibonacci(ind: int) -> int:
    f = [0, 1]
    for i in range(2, ind+1):
        f.append(f[i-1] + f[i-2])
    return f[ind]

print(fibonacci(10))
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
    for lis in data:
        if type(lis) == list:
            summary += recursely_sum_list(lis)
        else:
            summary = summary + lis
    return summary


print(nest_nums)
print(recursely_sum_list(nest_nums))
