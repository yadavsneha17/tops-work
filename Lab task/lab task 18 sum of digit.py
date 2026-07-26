num=int(input("enter a number "))
count=0
num1=num
while num!=0:
   rem = num// 10
   "rem=== ",rem
   count+=1
   num=num // 10
   print(f"{num1} contains {count} digits")
