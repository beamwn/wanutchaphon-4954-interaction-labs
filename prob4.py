from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def load_image(self):
        pass

    @abstractmethod
    def save_image(self):
        pass

class Bitmap(Image):
    def save_image(self, name):
        print("saving bitmap file", name)
    
    def load_image(self, name):
        print("loading bitmap file", name)


class Jpeg(Image):
    def save_image(self, name):
        print("saving jpeg file", name)
    
    def load_image(self, name):
        print("loading jpeg file", name)

        
if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")