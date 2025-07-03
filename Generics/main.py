#        WITHOUT GENERICS
class Box:
    def __init__(self, content):
        self.content = content
    
    def get_content(self):
        return self.content
    

box1 = Box(132)
box2 = Box("Good")

print(box1.get_content())
print(box2.get_content())
     


   ##   With Generics

from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self,content):
        self.content = content

    def get_content(self):
        return self.content

int_box = Box[int](764)
print(int_box.get_content()) 

str_box = Box[str]("Hello")
print(str_box.get_content()) 


