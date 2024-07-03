from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass

    def __str__(self):
        return f'this is the tool'


class SelectionTool(Tool):
    def mouse_down(self):
        print("selection tool icon")

    def mouse_up(self):
        print("draw a dashed rectangle")

    def __str__(self):
        return f'this is the Selection tool'


class BrushTool(Tool):
    def mouse_down(self):
        print("Brush Tool icon")

    def mouse_up(self):
        print("draw a line")

    def __str__(self):
        return f'this is the Brush tool'


class EraseTool(Tool):
    def mouse_down(self):
        print("Erase Tool icon")

    def mouse_up(self):
        print("Erase a line")

    def __str__(self):
        return f'this is the Erase tool'


class Canvas:
    def __init__(self, tool: Tool):
        self._tool = tool

    @property
    def tool(self):
        return self._tool

    def mouse_down(self):
        self._tool.mouse_down()

    def mouse_up(self):
        self._tool.mouse_up()


canvas = Canvas(SelectionTool())
print(canvas.tool)
canvas.mouse_down()
canvas.mouse_up()

canvas = Canvas(EraseTool())
print(canvas.tool)
canvas.mouse_down()
canvas.mouse_up()


