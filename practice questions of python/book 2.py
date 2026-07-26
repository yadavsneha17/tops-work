class Book:
    def __init__(self, title, author, noofpages, price):
        self.title = title
        self.author = author
        self.noofpages = noofpages
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.author} - {self.noofpages} pages - ₹{self.price}"


lstbook = []

while True:
    print("\n1. Add Book")
    print("2. Update Book")
    print("3. Search Book")
    print("4. View All Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            title = input("Enter title: ")
            author = input("Enter author: ")
            pages = int(input("Enter number of pages: "))
            price = float(input("Enter price: "))

            b = Book(title, author, pages, price)
            lstbook.append(b)

            print("Book added successfully.")

        case 2:
            search = input("Enter title to update: ")

            for b in lstbook:
                if b.title.lower() == search.lower():
                    b.author = input("Enter new author: ")
                    b.noofpages = int(input("Enter new number of pages: "))
                    b.price = float(input("Enter new price: "))
                    print("Book updated successfully.")
                    break
            else:
                print("Book not found.")

        case 3:
            search = input("Enter title to search: ")

            for b in lstbook:
                if b.title.lower() == search.lower():
                    print("\nBook Found:")
                    print(b)
                    break
            else:
                print("Book not found.")

        case 4:
            if len(lstbook) == 0:
                print("No books available.")
            else:
                print("\nAll Books:")
                for b in lstbook:
                    print(b)

        case 5:
            print("Exit")
            break

        case _:
            print("Invalid Choice")
