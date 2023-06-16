# inn=int(input("Eneter the number:"))
list1=['thumb','index','middle','ring','little']
while(True):
    inn=int(input("Eneter the number:"))
    if (inn<6):
        print("the {} had relation with {} finger".format(inn,list1[inn-1]))
    else:
        a=(inn-5)%4
        b=((inn-1)//4)%2
        print('a and b:',a,"  ",b)
        if(b==1):
            print("the {} had relation with {} finger".format(inn,list1[-a-1]))
        elif(b==0):
            print("the {} had relation with {} finger".format(inn,list1[a]))
      

    