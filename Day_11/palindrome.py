def pal_fun(s,l,r):
    n = len(s)
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return pal_fun(s,l+1,r-1)


s = "nitin"
l=0
r=len(s)-1

print(pal_fun(s,l,r))