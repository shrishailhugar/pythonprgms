s1 = "listena"
s2 = "silent"
sa = sorted(s1)
sb = sorted(s2)
print(sa)
print(sb)
if sa == sb:
    print("these are anagrams")

with open("input.txt",'r') as f, \
    open('output.txt', 'w') as op:
    # print(type(f.read()))
    text = f.readlines()
    up = [t.upper() for t in text]
    op.writelines(up)
with open("output.txt", "a") as f:
    f.writelines(text)

f = open("output.txt", "r")

print(type(f))

with open('C:\\Users\\ninga\Desktop\Shree\input.txt', 'rt') as inpf, \
    open('C:\\Users\\ninga\Desktop\Shree\output.txt', 'wt') as opf:
    text=inpf.read()

it=iter({'foo': 1, 'bar': 2, 'baz': 3})
# print(next(it))
dicta = dict(it)
print(dicta)



