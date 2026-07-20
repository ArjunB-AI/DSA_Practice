def head_recursion(n):
    if n == 0:
        return

    head_recursion(n - 1)  # Recursive call first
    print(n)


head_recursion(5)