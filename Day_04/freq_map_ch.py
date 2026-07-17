def common_ch(str1,str2):
    n = str1
    m = str2
    result = []
    freq_map = {}

    # building freq_map
    for i in n:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    print("frequency_map : ",freq_map)

    # Matching
    for i in m:
        if i in freq_map and freq_map[i] > 0:
            result.append(i)
            freq_map[i] -= 1
    
    return result


s1 = "apple"
s2 = "pppple"

print(common_ch(s1, s2))