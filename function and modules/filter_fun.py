def even(num):
    if num%2==0:
        return num
lst=[1,33,22,45,54,23]
lst_ans=list(filter(even,lst))
print(lst_ans)