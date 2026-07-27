name=input("enter a name: ")
for i in range(len(name)):
    print(name[i],"---->",i)
    # when we skip the one letter
    print(name[::2])
    # #when we want only middle part of the name
    print(name[1:-1])
    # #when we use indexing
    print(name[0:4])
    # #from where we want then we use indexing(3:)
    print(name[3:])
    print(name[:4])
    print(name[1:7]," ",name[1:7:2])
    print(name[::-1])
    print(name[:-1])



 