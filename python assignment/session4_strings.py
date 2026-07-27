# SESSION 4 - Strings Assignment
#----------------------  
# Task 1
#----------------------
product = "Redmi Note 12 Pro"

print("Task 1")
print("Uppercase:", product.upper())
print("Lowercase:", product.lower())


# Task 2
def clean_brand_name(name):
    return name.strip().replace("-", " ")

print("\nTask 2")
print(clean_brand_name(" oneplus-Nord "))


# Task 3
phone = "Apple iPhone 14 Pro Max"

txt = phone.split()
brand = phone[:len(txt[1])]
model = phone[len(txt[0]) + 1:]

print("\nTask 3")
print("Brand:", brand)
print("Model:", model)


# Task 4
def format_product_display(name, price):
    return f"{name} - {price}"

print("\nTask 4")
print(format_product_display("Boat Earbuds", 1299))


# Task 5
products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

electronic_items = []

for product in products:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()
    electronic_items.append(product)

print("\nTask 5")
print(electronic_items)
