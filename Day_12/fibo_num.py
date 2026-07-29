def fibo_num(num):
    if num == 0 or num == 1:
        return num
    return fibo_num(num-1) + fibo_num(num-2)


print(fibo_num(12))
print(fibo_num(13))
print(fibo_num(14))
print(fibo_num(15))