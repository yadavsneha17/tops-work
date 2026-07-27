def longest_string(string):
    longest = string[0]
    for s in string:
        if len(s) > len(longest):
            longest = s
    return longest
lst = ["tiger", "riano", "dog", "lion"]
print(longest_string(lst))


# def longest_string(strings):
#     return max(strings, key=len)

# words = ["cat", "lion", "dog", "giraffe"]
# print(longest_string(words))