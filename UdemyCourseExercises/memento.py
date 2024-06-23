# ### Document Memento ### #
from typing import List


class DocumentMemento:
    def __init__(self, content, font_name, font_size):
        self._content = content
        self._font_name = font_name
        self._font_size = font_size

    @property
    def content(self):
        return self._content

    @property
    def font_name(self):
        return self._font_name

    @property
    def font_size(self):
        return self._font_size


# ### Document ### #
class Document:
    def __init__(self):
        self._content = ""
        self._font_name = ""
        self._font_size = 0

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Font Size must be numeric")
        self._font_size = value

    def __str__(self):
        return f"Document attributes are: {self._content} & {self._font_name} & {self._font_size}"

    def create_document_memento(self) -> DocumentMemento:
        return DocumentMemento(self._content, self._font_name, self._font_size)

    def restore_document_memento(self, doc_mem: DocumentMemento):
        self._content = doc_mem.content
        self._font_name = doc_mem.font_name
        self._font_size = doc_mem.font_size


# ### History ### #
class History:
    def __init__(self):
        self._document_states: List[DocumentMemento] = []

    def push(self, doc_mem: DocumentMemento):
        self._document_states.append(doc_mem)

    def pop(self) -> DocumentMemento:
        return self._document_states.pop()


# ### Main Program ### #
my_doc = Document()
history = History()

my_doc.content = 'salam'
history.push(my_doc.create_document_memento())

my_doc.font_name = 'Tahoma1'
history.push(my_doc.create_document_memento())

my_doc.font_size = 1

print(my_doc)
my_doc.restore_document_memento(history.pop())
print(my_doc)
my_doc.restore_document_memento(history.pop())
print(my_doc)

