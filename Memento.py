from typing import List


# ### MEMENTO ______________________________
class EditorState:
    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content


# ### ORIGINATOR ___________________________
class Editor:
    def __init__(self):
        self._content = ""

    def get_content(self) -> str:
        return self._content

    def set_content(self, content: str):
        self._content = content

    def create_state(self) -> EditorState:
        return EditorState(self._content)

    def restore_state(self, state: EditorState):
        self._content = state.get_content()


# ### CARETAKER ___________________________
class History:
    def __init__(self):
        self._states: List[EditorState] = []

    def push(self, state: EditorState):
        self._states.append(state)

    def pop(self):
        if not self._states:
            raise IndexError("No state in history")
        return self._states.pop()


# ### THE MEMENTO PATTERN IN ACTION
if __name__ == "__main__":
    editor = Editor()
    history = History()

    editor.set_content('a')
    history.push(editor.create_state())

    editor.set_content('b')
    history.push(editor.create_state())

    editor.set_content('c')
    print(f'Current content is: {editor.get_content()}')

    editor.restore_state(history.pop())
    print(f'restored content is: {editor.get_content()}')

    editor.restore_state(history.pop())
    print(f'restored content is: {editor.get_content()}')


    print(editor.get_content())
