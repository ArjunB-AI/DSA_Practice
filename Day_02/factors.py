# def factors_num(num):
#     result = []
#     for i in range(1,(num//2 +1)):
#         if num % i == 0:
#             result.append(i)
#     result.append(num)
#     return result

# print(factors_num(25))


# -------------------------------------------------------------------------------
from math import sqrt
def factors_num(num):
    result = []
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num // i == i:
                result.append(num//i)
    return result