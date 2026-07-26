def odd_length_strings(lst):
    result = []
    for word in lst:
        if len(word)%2!=0:
            result.append(word)
    return result

strings=["Apple", "Banana", "Cat", "Dog", "Orange"]
print(odd_length_strings(strings))