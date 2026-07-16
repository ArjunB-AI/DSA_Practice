# def freq_map(num):
#     n = len(num)
#     result = {}
#     for i in range(0,n):
#         if num[i] in result:
#             result[num[i]] +=1
#         else:
#             result[num[i]] = 1
#     return result


# Method 2
def freq_map(num):
    n = len(num)
    result = {}
    for i in range(0,n):
        result [num[i]] = result.get(num[i],0) + 1
    return result


lst = [1,2,3,4,5,1,2,3,5,6,4,4]
print(freq_map(lst))