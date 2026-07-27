# SESSION 6 - Dictionaries & Sets

# Task 1: Create and print dictionary
playlist_prices = {
    "Top Hits": 199,
    "Chill Vibes": 149,
    "Workout Mix": 249,
    "Love Songs": 179,
    "Party Beats": 299
}

print("Original Dictionary:")
print(playlist_prices)


# Task 2: Update playlist price
def update_playlist_price(playlist, new_price):
    if playlist in playlist_prices:
        playlist_prices[playlist] = new_price
    else:
        print("Playlist not found!")

update_playlist_price("Workout Mix", 279)

print("\nDictionary after updating price:")
print(playlist_prices)


# Task 3: Delete a playlist
del playlist_prices["Love Songs"]

print("\nDictionary after deleting a playlist:")
print(playlist_prices)


# Task 4: Set operations
set1 = {"Domino's", "McDonald's", "Subway", "Pizza Hut"}
set2 = {"Subway", "Burger King", "Pizza Hut", "KFC"}

print("\nUnion of sets:")
print(set1.union(set2))

print("\nIntersection of sets:")
print(set1.intersection(set2))