s= "101010"
s=s[::-1]
tot=0
for i in range(0,len(s)):
    tot+=pow(2,i)*int(s[i])
print(tot)
