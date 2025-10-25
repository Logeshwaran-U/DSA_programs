
class add_binary:
    def bi_to_digit(self,x) ->int:
        a=x
        a=a[::-1]
        tot=0
        for i in range(0,len(a)):
            tot+=pow(2,i)*int(a[i])
        return tot

    def add_dgt_binary(self,x,y):
        tot =self.bi_to_digit(x)+self.bi_to_digit(y)
        op=""
        while tot>0:
            op = str(tot%2)+op
            tot//=2
        if op=="":
            return 0
        else:
            return op
        


r1 =add_binary()
print(r1.add_dgt_binary("11","1"))
print(r1.add_dgt_binary("0","0"))

