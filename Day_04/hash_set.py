def common_ele(lst1,lst2):

    n = lst1
    m = lst2

    hash_set = set(n)
    result = []

    for i in m:
        if i in hash_set:
            result.append(i)
    
    return result


l1 = [1,2,3,4,5]
l2 = [2,3,4]
print(common_ele(l1,l2))