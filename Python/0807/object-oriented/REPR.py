class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn
    def __repr__(self):
        return "ISBN:"+self.__isbn+"\n"+"Name:"+self.__title
book = Book("The Python Tutorial", "442456789")
print(book)