def common_ele(lst1,lst2):

    n = lst1
    m = lst2
    hash_map = {}

    for num in n:
        hash_map[num] = True

    result = []

    for k in m:
        if k in hash_map:
            result.append(k)
    
    return result


l1 = [1,2,3,4,5]
l2 = [2,3,4]
print(common_ele(l1,l2))