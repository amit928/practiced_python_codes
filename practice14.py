# from abc import ABC
# class abst(ABC):
#     def test(self):
#         print("Test method")

# Ab=abst()
# Ab.test()

from abc import ABC,abstractmethod
class abst(ABC):
    @abstractmethod
    def test(self):
        print("Test method1")

class abst2(abst):
    def test(self):
        print("Testing")
    def develop(self):
        print("Developing")

Ab=abst2()
Ab.test()
Ab.develop()
