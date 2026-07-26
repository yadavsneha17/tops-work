list = []
for i in range(5):
    name = input(f"Enter name: ")
    list.append(name)
print("List of names:", list)
for name in list:
    print(name, len(name))
index = int(input("Enter a index to remove: "))
list.pop(index)
print("Updated list:",list) 