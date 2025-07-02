from dataclasses import dataclass , field

@dataclass
class Person :
    name:str
    age:int
    email: str | None
    field: list[str] = field(default_factory= list)


    def is_adult(self) -> bool:
        """Example  method that uses data class attributes. """
        return self.age >= 18
    

    
#                """Bad Practice to write a code"""

# class Person:
#     def __init__(self, name: str, age: int, email: str | None, field=None):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.field = field if field is not None else []

#     def is_adult(self) -> bool:
#         return self.age >= 18

#     def __repr__(self):
#         return (
#             f"Person(name='{self.name}', age={self.age}, "
#             f"email='{self.email}', field={self.field})"
#         )


def demo_good_usage():
    Person1 = Person(name="abdul", age = 17, email="google@gmail.com")
    Person3 = Person(name="zara", age=19, email="zara@gmail.com")
    Person4 = Person(name="hassan", age=23, email="hassan@example.com")
    
    Person1.field.append("Developer")

    print(f"Person1 : {Person1}")
    print(f"Person3 : {Person3}")
    print(f"Person4 : {Person4}")

    print(f"Is {Person3.name} Adult: {Person3.is_adult()}")


if __name__ == "__main__":
    demo_good_usage()





