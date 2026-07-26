name=input("enter a name: ")
rev = name[::-1]
name = rev[0] + name[1:-1] + name[0]
print(name)



