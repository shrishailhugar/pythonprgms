def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

string="let me check"

indlist=(findOccurrences(string, ' '))

# print(round(12474,-3))

# text="Sathwik"
# print(f'{tuple1[0]:_^20}')
# print(f'{text:*>50}')
# print(text.center(20,"8"))

print(string.count(" ",3,5))
stlist=string.split(" ")
print(stlist)

nspstring="".join((stlist))
nspstring="".join(reversed(nspstring))

print(nspstring)
