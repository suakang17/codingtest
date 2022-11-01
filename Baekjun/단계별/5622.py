# chrlist = [i for i in (map(chr, range(65, 91)))]
# print(chrlist)
chrlist = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
time = 0
for c in input():
    for i in chrlist:
        if c in i:
            time += chrlist.index(i) + 1 + 2
print(time)

# 타 소스 - enumerate 사용
a = {c: i for i, cs in enumerate(("ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"), 3) for c in cs}
print(sum(a[c] for c in input()))