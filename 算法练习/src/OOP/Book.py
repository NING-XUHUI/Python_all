class Book(object):
    def __init__(self, name=str, price=float, author=str, publisher=str):
        self.__name = name
        self.__price = price
        self.__author = author
        self.__publisher = publisher

    def set_author(self, author=str):
        self.__author = author

    def set_name(self, name=str):
        self.__name = name

    def set_price(self, price=float):
        self.__price = price

    def set_publisher(self, publisher=str):
        self.__publisher = publisher


