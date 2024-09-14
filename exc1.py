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

# print(list(map(NWD, numbers)))
print("nwd", nwd_recursive(14, 12))

