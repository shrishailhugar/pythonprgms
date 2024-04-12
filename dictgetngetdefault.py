dict1={'a':"shreee",'b':"Bapu"}

#here  if the key present it' going to get that value else it will print default value
print(dict1.get('a','sh'))
print(dict1)

#settig default here the a key value not going to overwritten by 'manu' instead it will be shree only.
#if there is a value present don't overwrite else write.
dict1.setdefault('a',"Manu")
print(dict1)
