
n1=10
c=""
while n1>0:
    c= str(n1%2)+c
    n1//=2

print(c)

tot=0
for i in range(0,len(c)):
    tot+=pow(2,i)*int(c[i])
print(tot)
