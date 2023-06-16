with open('input.txt','r') as reader,\
  open('output.txt','w')as writer:
    # for txt file(r) type file readinng or writing object will be TEXTIOWrapper
    print(type(reader),"$$$$$",type(writer))
    for line in reader:
        listline=line.split(" ")
        capatilized_line=[x.capitalize() for x in listline]
        capatilized=" ".join(capatilized_line)
        writer.writelines(capatilized)


with open('pythonselenium.png','rb')as reader,\
    open("output2.png","wb")as writer:
    # for binary file(b) type file readinng or writing object will be BufferedReader and BufferedWriter
    print(type(reader),"$$$$$",type(writer))
    for line in reader:
            #  print(line," ",type(line))
            #  writer.writelines(line)
            ...