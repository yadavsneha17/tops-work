def converttocelcius(ferenit):
    return ((ferenit-32)*(5/9))
lst=[98.6,90.0,300.9]
lst_cel=[]
for i in lst:
    lst_cel.append(converttocelcius(i))



lst_base=[1,2,3,4]
lst_pow=[2,3,1]
lst_ans=list(map(pow,lst_base,lst_pow))
print(lst_ans)




    