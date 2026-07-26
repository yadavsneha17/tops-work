start=int(input("enter a start number: "))
end=int(input("enter a end number: "))
sum = 0
for i in range(start,end+1):
    if i%5==0 and i%7==0:
        sum += 1
print("sum: ",sum) 