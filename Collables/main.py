from dataclasses import dataclass
from typing import Callable

@dataclass
class Calculator:
    operations:Callable[[int,int],str]

    def calculate(self,a:int,b:int)-> str:
        return self.operations(a,b)
    
    # def __call__(self,a:int,b:int)-> str:
    #     return self.operations(a,b)
    

def add_and_stringify(a:int,b:int)-> str:
    return str(a + b)

cal = Calculator(operations=add_and_stringify)
print(cal.calculate(23,23))
# print(cal(23,23))


if __name__ == "__main__":
    pass

