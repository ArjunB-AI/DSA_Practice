def tail_recursion(n):
    if n == 0:
        return

    print(n)
    tail_recursion(n - 1)  # Recursive call last


tail_recursion(5)