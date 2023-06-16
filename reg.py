import re
pattern='[+*/-][+*/-]+'
string='1+23-+4*/*9'
# x=re.sub('[+*/-][+*/-]+','@',string)
# x=re.search(pattern,string)
# print(x)
# print(x.span())

y=re.findall(pattern,string)
print(y)
for a in y:
    string=string.replace(a,a[0])
    print(string)

print(eval(string))
# 1+23-+4*/9
# 1+23@ 4* 9