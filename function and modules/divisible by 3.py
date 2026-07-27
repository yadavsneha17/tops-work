def divisible_by_3(lst):
    result = []
    for i in lst:
        if i % 3 == 0:
            result.append(i)
    return result
lst=[11,12,13,14,15,23]
print(divisible_by_3(lst))


