from typing import List, Tuple
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def has_previous(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def current(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def next(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def previous(self) -> None:
        raise NotImplementedError


class BrowseHistory:
    def __init__(self):
        # self._urls: List[str] = []
        self._urls: Tuple[str, ...] = ('',)

    def push(self, url: str) -> None:
        # self._urls.append(url)
        self._urls = self._urls + (url, )

    def pop(self) -> str:
        # return self._urls.pop()
        temp = list(self._urls)
        last_item = temp.pop()
        self._urls = tuple(temp)
        return last_item

    def create_iterator(self, index: int) -> Iterator:
        return ListIterator(self, index)


    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, history):
        self._urls = history


class ListIterator(Iterator):
    def __init__(self, browse_history: BrowseHistory, index):
        self._browse_history = browse_history
        self._index = index

    def has_next(self) -> bool:
        return self._index < len(self._browse_history.urls)

    def has_previous(self) -> bool:
        return self._index >= 0

    def current(self) -> str:
        return self._browse_history.urls[self._index]

    def next(self) -> None:
        self._index += 1

    def previous(self) -> None:
        if self._index >= 0:
            self._index -= 1


browse_history = BrowseHistory()
browse_history.push('a')
browse_history.push('b')
browse_history.push('c')
browse_history.push('d')
browse_history.pop()
browse_history.push('salam')

print('Forward')

iterator = browse_history.create_iterator(0)
while iterator.has_next():
    print(iterator.current())
    iterator.next()

print('Inverse')

iterator2 = browse_history.create_iterator(len(browse_history.urls)-1)
while iterator2.has_previous():
    print(iterator2.current())
    iterator2.previous()
