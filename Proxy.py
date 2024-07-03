# #### LAZY INITIALIZATION #### #
from abc import ABC, abstractmethod


class ImageSubject(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(ImageSubject):
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_image()

    def load_image(self):
        print(f"image {self.file_name} is loaded")

    def display(self):
        print(f'image {self.file_name} is displayed')


class ImageProxy(ImageSubject):
    def __init__(self, file_name):
        self.file_name = file_name
        self.real_image = None

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.file_name)
        self.real_image.display()


image1 = RealImage('salam')
image1.display()

image2 = ImageProxy('salam2')
image2.display()
