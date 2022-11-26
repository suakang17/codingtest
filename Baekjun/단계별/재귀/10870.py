n = int(input())
a = n
pib = [0, 1]
while n >= 0:
    pib.append(pib[-1]+pib[-2])
    n -= 1
print(pib[a])