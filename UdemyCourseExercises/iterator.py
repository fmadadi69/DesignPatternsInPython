from abc import ABC, abstractmethod


class Product:
    def __init__(self, pid, name):
        self._id = pid
        self._name = name

    def __str__(self):
        return f''' Product:( id = {self._id}, name = {self._name} )'''


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def current(self) -> Product:
        raise NotImplementedError

    @abstractmethod
    def next(self) -> None:
        raise NotImplementedError


class ProductCollection:
    def __init__(self):
        self._product: list[Product] = []

    def add(self, product: Product):
        self._product.append(product)

    def create_iterator(self):
        return ListIterator(self)

    @property
    def product(self):
        return self._product


class ListIterator(Iterator):
    def __init__(self, product_collection: ProductCollection):
        self._product_collection = product_collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._product_collection.product)

    def current(self) -> Product:
        return self._product_collection.product[self._index]

    def next(self) -> None:
        self._index += 1


# ### MAIN ### #
product_collection = ProductCollection()

product_collection.add(Product(1, 'Faezeh'))
product_collection.add(Product(2, 'Hussein'))
product_collection.add(Product(3, 'Maman'))
product_collection.add(Product(4, 'Baba'))

iterator = product_collection.create_iterator()

while iterator.has_next():
    print(iterator.current())
    iterator.next()

