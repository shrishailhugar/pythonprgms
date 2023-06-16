def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


print(findOccurrences("let me chek", ' '))

 
s1="Rohit"
print(s1)
print(id(s1))
s1=s1.replace("R","M")
# print(x)
print(id(s1))


list1=['x','y','z']
list2=['a','b']
dict1={}
listmerged=[[a,b] for a in(list1) for b in list2]
dict1["a"]="hero"
print(dict1.get("a"))


