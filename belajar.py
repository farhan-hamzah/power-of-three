n = int(input())
i = 0
j = 3
b = False
for i in range(n):
    j = j**i
    i +=1
    if j == n:
        b = True
        j = 3
    else:
        j = 3
print(b)
