from abc import abstractmethod, ABC


class Window(ABC):
    def close(self):
        self._before_close_method()
        print("CLOSEEEEEEEEEEE")
        self._after_close_method()

    @abstractmethod
    def _before_close_method(self):
        pass

    @abstractmethod
    def _after_close_method(self):
        pass


class WoodenWindow(Window):
    def _before_close_method(self):
        print("Before Close Wooden")

    def _after_close_method(self):
        print("After close Wooden")


class IronWindow(Window):
    def _before_close_method(self):
        print("Before Close Iron")

    def _after_close_method(self):
        print("After close Iron")


window = IronWindow()
window.close()
