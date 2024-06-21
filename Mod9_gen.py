
def all_variants(s):
    n = len(s)
    for i in range(1,n):
        subset = ""
        for j in range(n):
            if (i << j) > 0:
                subset += s[j]
        yield subset


a = all_variants("abc")
for i in a:
    print(i)
