def fib(num):
    if num < 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

def find_input():
    n = 1
    while True:
        value = fib(n)
        if value == 55:
            return n
        n += 1

print("Input that produces Fibonacci value of 55:", find_input())

