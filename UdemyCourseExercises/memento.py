from typing import List
# ### Content Memento ### #


class ContentMemento:
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content


# ### Font Name Memento ### #
class FontNameMemento:
    def __init__(self, font_name):
        self._font_name = font_name

    @property
    def font_name(self):
        return self._font_name


# ### Font Size Memento
class FontSizeMemento:
    def __init__(self, font_size):
        self._font_size = font_size

    @property
    def font_size(self):
        return self._font_size


# ### Originator ### #
class Document:
    def __init__(self):
        self._content = ""
        self._font_name = ""
        self._font_size = 0

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        self._font_name = font_name

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Font size must be numeric")
        self._font_size = value

    def __str__(self):
        return f"""
        Content = {self._content},
        Font Name = {self._font_name},
        Font Size = {self._font_size}
        """

    def create_content_state(self) -> ContentMemento:
        return ContentMemento(self._content)

    def restore_content_state(self, content_memento: ContentMemento):
        self._content = content_memento.content

    def create_font_name_state(self) -> FontNameMemento:
        return FontNameMemento(self._font_name)

    def restore_font_name_state(self, font_name_memento: FontNameMemento):
        self._font_name = font_name_memento.font_name

    def create_font_size_state(self) -> FontSizeMemento:
        return FontSizeMemento(self._font_size)

    def restore_font_size(self, font_size_memento: FontSizeMemento):
        self._font_size = font_size_memento.font_size


# ### CARETAKER ### #
class History:
    def __init__(self):
        self._content_states : List[ContentMemento] = []
        self._font_name_states : List[FontNameMemento] = []
        self._font_size_states : List[FontNameMemento] = []

    def push_content(self, content_memento:ContentMemento):
        self._content_states.append(content_memento)

    def pop_content(self) -> ContentMemento:
        if not self._content_states:
            raise IndexError("No Content Memento in Content states")
        return self._content_states.pop()

    def push_font_name(self, font_name_memento: FontNameMemento):
        self._font_name_states.append(font_name_memento)

    def pop_font_name(self) -> FontNameMemento:
        if not self._font_name_states:
            raise IndexError("No Font name memento in Font Name States")
        return self._font_name_states.pop()

    def push_font_size(self, font_size_memento:FontSizeMemento):
        self._font_size_states.append(font_size_memento)

    def pop_font_size(self):
        return self._font_size_states.pop()


# ### Main ### #
if __name__ == "__main__":
    doc = Document()
    hist = History()

    doc.content = 'salam'
    doc.font_name = 'b nazanin'
    doc.font_size = 18
    hist.push_content(doc.create_content_state())
    hist.push_font_name(doc.create_font_name_state())
    hist.push_font_size(doc.create_font_size_state())
    print(f'Current State is : {doc.content} & {doc.font_name} & {doc.font_size}')

    doc.content = 'khubi?'
    doc.font_name = 'Tahoma'
    doc.font_size =19
    hist.push_content(doc.create_content_state())
    hist.push_font_name(doc.create_font_name_state())
    hist.push_font_size((doc.create_font_size_state()))
    print(f'Current State is : {doc.content} & {doc.font_name} & {doc.font_size}')

    doc.content = 'Bye'
    doc.font_name = 'Mitra'
    doc.font_size = 20
    doc.restore_content_state(hist.pop_content())
    hist.push_font_name(doc.create_font_name_state())
    doc.restore_font_size(hist.pop_font_size())
    print(f'Current State is : {doc.content} & {doc.font_name} & {doc.font_size}')

    doc.restore_content_state(hist.pop_content())
    doc.restore_font_name_state(hist.pop_font_name())
    doc.restore_font_size(hist.pop_font_size())
    print(f'Current State is : {doc.content} & {doc.font_name} & {doc.font_size}')




