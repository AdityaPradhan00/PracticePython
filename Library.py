class Library:
    def __init__(self, lisst, name):
        self.booksList = lisst
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"\nWe have following books in our library: {self.name}")
        i = 0
        for book in self.booksList:
            i = i + 1
            print(f"{i}. {book}")

    def lendbook(self, user, book):
        if book not in self.booksList:
            print("Book not present in Library")
        elif book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    list_books = ['Python', 'C', 'C++', 'C#', 'BlueJ']
    Name = input("Enter the name of the library: ")
    lib = Library(list_books, Name)

    while True:
        print(f"\nWelcome to the {Name} library.")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input("Enter your choice to continue: ")
        if user_choice not in ['1', '2', '3', '4']:
            print("\nPlease enter a valid option")
            continue

        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            lib.displaybooks()

        elif user_choice == 2:
            user = input("\nEnter your name: ")
            book = input("Enter the name of the book you want to lend: ")
            lib.lendbook(user, book)

        elif user_choice == 3:
            book = input("\nEnter the name of the book you want to add: ")
            lib.addbook(book)

        elif user_choice == 4:
            book = input("\nEnter the name of the book you want to return: ")
            lib.returnbook(book)

        else:
            print("Not a valid option")

        print("\nPress q to quit and c to continue: ")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
            else:
                print("wrong input")
