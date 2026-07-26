def lngst_string(lst):
    lst1 = lst[0]
    for i in lst:
        if len(i) > len(lst1):
            lst1 = i
    return lst1
print(lngst_string(["pen", "notebook", "book"]))