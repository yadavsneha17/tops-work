def divisible(lst):
    new = []
    for i in lst:
        if i % 2 == 0 and i % 3 == 0:
            new.append(i)
    return new

print(divisible([2, 6, 9, 12, 18, 25]))