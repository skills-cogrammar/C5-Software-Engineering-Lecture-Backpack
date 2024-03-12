class Book:

    def __init__(self, title, author, genre, quantity):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__quantity = quantity

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author
    
    def set_genre(self, genre):
        self.__genre = genre
    
    def get_genre(self):
        return self.__genre
    
    def increase_quantity(self, value):
        self.__quantity += value

    def decrease_quantity(self, value):
        self.__quantity -= value

    def get_quantity(self):
        return self.__quantity
    
    def is_available(self):
        return self.__quantity > 0
    
    def details(self):
        details = f"Title:\t{self.__title}\n"
        details += f"Author:\t{self.__author}\n"
        details += f"Genre:\t{self.__genre}\n"
        details += "Available: "
        details += "Yes\n" if self.is_available() else "No\n"
        return details
    
    def __str__(self):
        return f"{self.__title}\t\t{self.__author}"
    

