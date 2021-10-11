from os.path import isfile

class Book(object):
    """ class for a single Book object """

    def __init__(self, title, author, year, filename):
        """ constructor for book object, given title, author, year, and filename """

        self.title = title
        self.author = author
        self.year = year
        self.filename = filename
        self.bookmark = 0

    def __str__(self):
        """ pretty-print info about this object """
        print(self.toString)

    def getTitle(self):
        """ getter for book title """
        return self.title

    def getAuthor(self):
        """ getter for book title """
        return self.author

    def getYear(self):
        """ getter for book year """
        return self.year

    def getFilename(self):
        """ getter for book filename """
        return self.filename

    def getBookmark(self):
        """ getter for bookmark """
        return self.bookmark

    def setBookmark(self, bookmark):
        """ setter for bookmark """
        self.bookmark = bookmark

    def toString(self):
        """ pretty-print info about this book """
        return "%25s by %20s (%i)" % (self.title, self.author, self.year)

    def getText(self):
        """ get the book's text as a string from file """
        bookFile = open(self.filename, "r")
        bookText = ""
        for line in bookFile:
            # Exclude commented lines
            if not line[0] == "#":
                bookText += line
        bookFile.close()
        return bookText


if __name__ == '__main__':
    print("Testing the Book class...")
    myBook = Book("Gettysburg Address", "Abe Lincoln", 1863, "book-database/alice.txt")

    print("Testing toString...")
    print(myBook.toString())

    print("Testing getFilename...")
    print(myBook.getFilename())

    print("Testing getText...")
    text = myBook.getText()
    print(text[:105])                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())

    # Test toString formatting
    myBook2 = Book("Ulysses", "James Joyce", 1922, "book-database/ulysses.txt")
    print("Testing toString formatting...")
    print(myBook.toString())
    print(myBook2.toString())
