def reverse_num(num):
    num = abs(num)
    
    if num == 0:
        return 0
    
    result = 0
    while num > 0:
        ld = num % 10
        result = (result*10) + ld
        num = num // 10
    return result

print(reverse_num(12345))