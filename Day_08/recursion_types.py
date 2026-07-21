# Functional recursion and Parameterized recurion.

# Q - Sum of N ntural numbers

# 1 - Parameterized recursion
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)

print(func(0,1,5))

# 2 - Functional Recursion
def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

print(func(5))
