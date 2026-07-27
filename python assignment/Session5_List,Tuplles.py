# SESSION 5 - Lists & Tuples

# Task 1
print("Task 1")
playlist_ids = [1, 2, 3, 4, 5]
playlist_ids.append(6)
print(playlist_ids)


# Task 2
print("\nTask 2")

cart_items = ["t-shirt", "shoes"]
cart_items.extend(["jeans", "cap"])

print(cart_items)


# Task 3
print("\nTask 3")

def remove_last_item(order_list):
    item = order_list.pop()
    return item

order_list = ["Pizza", "Burger", "Fries"]

print("Removed Item:", remove_last_item(order_list))
print("Order List:", order_list)


# Task 4
print("\nTask 4")

insta_filters = ("Normal", "Clarendon", "Juno", "Lark")

# Tuples cannot be changed.
# insta_filters[1] = "Aden"   # TypeError

print(insta_filters)


# Task 5
print("\nTask 5")

favorite_genres = ["Pop", "Rock", "Hip Hop"]     # List
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")   # Tuple

print("Favorite Genres:", favorite_genres)
print("Train Classes:", train_classes)

print("List is used because genres can change.")
print("Tuple is used because train classes are fixed.")