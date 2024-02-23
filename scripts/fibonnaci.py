def func4(param_1):
    if param_1 < 2:
        return 1
    else:
        return func4(param_1 - 1) + func4(param_1 - 2)

def find_input_for_fib_55():
    param_1 = 1
    while True:
        fibonacci_value = func4(param_1)
        if fibonacci_value == 55:
            return param_1
        param_1 += 1

input_for_fib_55 = find_input_for_fib_55()
print("Input that produces Fibonacci value of 55:", input_for_fib_55)

