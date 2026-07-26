class book():
    def _init_(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.noofpages=pages
        self.price=price
    def _str_(self):
        return f"{self.title} - {self.author} - {self.noofpages} - {self.price}"    

lstbook=[]

while True:
    print("1. add book ")
    print("2. Upadte book")
    print("3. search book ")
    print("4. view all book ") 
    print("5. exit ")  
    choice=int(input("Enter a choice  = "))
    match choice:
        case 1:
            title=input("Enter title = ")
            author=input("Ente author = ")
            page=int(input("Enter page = "))
            price=int(input("Enter price = "))
            
            b = book (title, author, page, price)
            lstbook.append(b)   
        case 2:
            pass
        case 3:
            search = input("Enter title to search: ")

            for book in lstbook:
                if book.title == search:
                    print(book)
                    break
            else:
                print("Book not found.")
        case 4:
            print("TITLE")
            for book in lstbook:
                print(book)
        case 5:
            print("Exit")
            break

        case _:
            print("Invalid Choice")



        

