class BookShelf:
    def __init__(self,name,author,price,publishing_year):
        self.book_name,self.book_author,self.book_price,self.book_publishing_year = name,author,price,publishing_year
    def addBook(self):
        print("Book name: " + self.book_name)
        print("Book Author: " + self.book_author)
        print("Book Price: "+ str(self.book_price))
        print("Book publishing year: "+str(self.book_publishing_year))
        print("Book Added")
    def years_since_published(self):
        var = 2022 - self.book_publishing_year
        print("This book is published "+ str(var) +" years ago")
b = BookShelf("Harry Potter and The Philosopher's Stone","J. K. Rowling", 1928,1997)
b.addBook() 
b.years_since_published()