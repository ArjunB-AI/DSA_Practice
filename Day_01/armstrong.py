def is_armstrong(num):
    original_num = num
    total = 0
    nod = len(str(num))
    while num > 0:
        ld = num % 10
        total = total + (ld ** nod)
        num = num // 10
    return total == original_num


# print(is_armstrong(101))
print(is_armstrong(153))