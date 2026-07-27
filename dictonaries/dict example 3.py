dict1={
 "name":"Kavyansh",
 "course":"DS",
 "address":"Paldi",
 "age":20,
 "name":"prince"
}
dict1["name"]="Vivek"
dict1["marks"]=120
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
for i,j in dict1.items():
    print(i,'--->',j)