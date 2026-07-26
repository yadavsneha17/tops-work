name = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": False},
    {"name": "Charlie", "age": 35, "active": True}
]
for i in name:
    if i["age"] >= 18:
        print(i["name"].upper())