def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest([100, 70, 99, 20]))