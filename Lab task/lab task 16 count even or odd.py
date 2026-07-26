num=int(input("enter a number: "))
count=0
even=0
odd=0
while num!=0:
    rem=num%10
    count+=1
    num=num//10
    if rem % 2==0:
        even+=1
    else:
        odd +=1
print(f"total digit: {count} ")
print(f"even digit: {even}")
print(f"odd digit: {odd}")

