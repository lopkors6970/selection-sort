a = [7,8,3,1,18,9,21,20,5,17]
k = 0
size = 10

while (k < size-1):
    min = a[k]
    i = 1
    while (i<size-k):
        if (a[i]<a[i-1]):
            temp = a[i]
            a[i] = a [i-1]
            a[i-1] = temp
        else:
            i+=1
    else:
        k+=1
print(a)
