a=[4,3,2,1,5,6,7,8]
l =len(a)//2
for i in range(0,l-1):
    for j in range(0,l-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

for i in range(l,len(a)):
    for j in range(l,len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
