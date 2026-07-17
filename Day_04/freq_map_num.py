# using frequency map

def common_ele(lst1,lst2):
    n = lst1
    m = lst2

    freq_map = {}
    result = []

    # building freq_map
    for i in n:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    
    print("frequency_map : ",freq_map)

    #match elements
    for i in m:
        if i in freq_map and freq_map[i] > 0:
            result.append(i)
        freq_map[i] -= 1
    
    return result

l1 = [1,2,3,4,5,2]
l2 = [2,3,4,2,2]

print(common_ele(l1,l2))