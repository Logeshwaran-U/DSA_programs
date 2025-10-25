
a="Logic"        
nw=""
for i in a:
    if i.lower() in "aeiou":
        nw+=chr(ord(i)+1)
    else:
        nw+=i
print(nw)
