def count_vowels(txt):
    count = 0
    for ch in txt:
        if ch in "aeiouAEIOU":
            count += 1
    return count
string = input("Enter a string: ")
print("No of vowels:", count_vowels(string))