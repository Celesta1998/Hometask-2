x=int(input())
list = []
c = 0
summa = 0
while c<x:
    c += 1
    list.append(c)
    summa += c
print(list)
print(sum(list))
print(summa)