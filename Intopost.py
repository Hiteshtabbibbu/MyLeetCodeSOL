'''
Infix to postfix
'''

#SOLUTION

li = []
p = {'*':2,'/':2,'+':1,'-':1,'!':3}
stmt = input("Enter statement: ")
res = ""
for i in stmt:
    if ord(i)>=97 and ord(i)<=122:
        res += i
    if i == '+' or i == '-' or i=='*' or i=='/' or i=='!':
        if li:
            if p[i] > p[li[len(li)-1]]:
                li.append(i)
            else:
                while(li and p[i]<=p[li[-1]]):
                    res+=li.pop()
                li.append(i)
        else:
            li.append(i)
while(li):
    res += li.pop()
print(res)
