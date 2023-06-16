import re

pattern1="[+*/-]{2}"
inputstring="4+-6-*8"
list=re.findall(pattern1,inputstring)
print(list)
for i in list:
    inputstring=inputstring.replace(i,i[1])

print(eval(inputstring))
pattern2="[+*/-]"
text=re.sub(pattern2,"",inputstring,count=2)
print(text)

