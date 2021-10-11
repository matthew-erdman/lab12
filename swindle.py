from book import *


def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for book in infile:
        bookInfo = book.split(',')
        # title, author, year, filename
        newBook = Book(bookInfo[0], bookInfo[1], int(bookInfo[2]), bookInfo[3].strip())
        availableBooks.append(newBook)

    return availableBooks


def getInteger(min, max, prompt):
    """
    Purpose: Gets input from the user and validates that it is a non-negative integer.
    Parameters: None.
    Return Value: The user's chosen integer.
    """
    userInt = input(prompt)
    while True:
        try:
            userInt = int(userInt)
            if min <= userInt <= max:
                return userInt
        except ValueError:
            pass
        print("Invalid input, try again")
        userInt = input(prompt)


class Swindle(object):
    """ class for a single Swindle object """

    def __init__(self, owner):
        """ constructor for swindle object, given owner """
        self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
        self.owner = owner
        self.ownedBooks = []
        self.pageLength = 20


    def __str__(self):
        """ pretty-print info about this object """
        s = "%s's Swindle v1.0" % self.owner
        return s


    def getOwner(self):
        """ getter for Swindle owner """
        return self.owner


    def getLetter(self):
        """ This method determines what the user wants to do next """
        validChoices = ['n', 'p', 'q']
        while True:
            readingChoice = str(input("\nn (next); p (previous); q (quit): "))
            if readingChoice in validChoices:
                return readingChoice
            print("invalid input, try again")


    def displayPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        for i in range(pageStart, pageEnd):
            print(bookLinesList[i])
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, numPages))
        return


    def displayText(self, book):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        while True:
            self.displayPage(book)
            currentPage = book.getBookmark()
            choice = self.getLetter()       # user chooses to quit or read the next/previous page
            if choice == "q":               # quit reading and return to ereader
                return book
            elif choice == "n":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:                               # return to previous page in the book
                book.setBookmark(currentPage-1)
        return


    def showAvailable(self):
        """ List the books available for purchase (that the user doesn't own) """
        if len(self.availableBooks) > 0:
            print("\nAvailable books:")
            for i in range(len(self.availableBooks)):
                print("%i: %s" % (i+1, self.availableBooks[i].toString()))
        else:
            print("\nThere aren't any books available to purchase!")


    def showOwned(self):
        """ List the books owned by the user """
        if len(self.ownedBooks) > 0:
            print("\nBooks you own:")
            for i in range(len(self.ownedBooks)):
                print("%i: %s" % (i+1, self.ownedBooks[i].toString()))
        else:
            print("\nYou don't own any books!")


    def buy(self):
        """ List the books available for purchase and have the user select one to own """
        self.showAvailable()
        if len(self.availableBooks) > 0:
            prompt = "\nWhich book would you like to buy? (0 to skip): "
            bookNum = getInteger(0, len(self.availableBooks), prompt)
            if bookNum == 0:
                return 0
            else:
                book = self.availableBooks[bookNum-1]
                self.availableBooks.remove(book)
                self.ownedBooks.append(book)
                print("\nYou've successfully purchased the book: %s" % book.getTitle())


    def read(self):
        """ List the books owned and have the user select one to read through displayText() """
        self.showOwned()
        if len(self.ownedBooks) > 0:
            prompt = "\nWhich book would you like to read? (0 to skip): "
            bookNum = getInteger(0, len(self.ownedBooks), prompt)
            if bookNum == 0:
                return 0
            else:
                book = self.displayText(self.ownedBooks[bookNum-1])
                print("\nSetting bookmark in %s at page %i" % (book.getTitle(), book.getBookmark()))



if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Matthew"
    myswindle = Swindle(owner)
    print(myswindle)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    print("------------------------")
    print("Testing buy...")
    myswindle.buy()

    print("------------------------")
    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("------------------------")
    print("Testing read...")
    myswindle.read()
