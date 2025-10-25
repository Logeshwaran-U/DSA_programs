
s ="a12eiou5erwrwe12A2ee0ezezwz33"
nw=""
v=""
sm=""

s.lower()
for i in s:
    if i in "1234567890":
        nw+=i
    elif(i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u" ):
        v+=i
    else:
        sm+=i
print(nw+v+sm)
