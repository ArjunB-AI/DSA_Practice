# N = 1234
# count = 0
# num = N
# while num > 0:
#     count += 1
#     num = num // 10
# print(count)

def count_num(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        count +=1
        num = num // 10
    return count

print(count_num(12345))