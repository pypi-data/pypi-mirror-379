def fibonacci_py(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_py(n - 1) + fibonacci_py(n - 2)