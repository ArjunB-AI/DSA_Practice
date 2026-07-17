def common_ch(str1,str2):
    n = str1
    m = str2
    result = []
    hash_map = {}

    for i in str1:
        hash_map[i] = True
    
    for k in str2:
        if k in hash_map:
            result.append(k)
    
    return result

s1 = "apple"
s2 = "pple"

print(common_ch(s1,s2))