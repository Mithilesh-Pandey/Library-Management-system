class Library:
    def __init__(self,list,name):
        self.bookList=list
        self.name=name
        self.lendDict={}

    def displayBook(self):
        print(f"We have following books in our library: {self.name} ")
        for book in self.bookList:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.you can take the book now ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")    

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)   

if __name__=="__main__":
    mithilesh=Library(["Python","Rich Daddy Poor Daddy","Javascript","Atomic Habbit"],"Mithilesh_Library")
    while(True):
        print(f"Welcome to the {mithilesh.name}.Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return a Book")
        user_choice=input()

        if user_choice not in ["1","2","3","4"]:
            print("Please enter a valid option")
            continue

        else:
            user_choice=int(user_choice)


        if user_choice==1:
            mithilesh.displayBook()

        elif user_choice==2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name:")
            mithilesh.lendbook(user,book)

        elif user_choice==3:
            book=input("Enter the name of the book you want to add:")
            mithilesh.addBook(book)
            
        elif user_choice==4:
            book=input("Enter the name of the book you want to return:")
            mithilesh.returnBook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue ")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()  

            elif user_choice2=="c":
                continue      