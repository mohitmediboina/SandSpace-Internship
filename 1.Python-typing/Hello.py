from typing import Optional, Any


# Today i learned about python typing module to enable type hints in python.
# Type hints are a way to indicate the expected data types of variables, 
# function parameters, and return values. They can help improve code readability 
# and catch potential bugs during development.

# using mypy package and vs code extension to see the typing errors in my code.

# also learned this module is not used for runtime type checking,
# but rather for static analysis and documentation purposes.


# Here are some examples of how to use type hints in Python:


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return "Hello " + name


x: int = 10
y: float = 3.14
name: str = "Mohit"
flag: bool = True


# for 3.8 and earlier, you can use the following syntax for type hints:
from typing import List, Tuple, Set, Dict

nums: List[int] = [1, 2, 3]
point: Tuple[int, int] = (2, 3)
unique: Set[int] = {1, 2, 3}
mapping: Dict[str, int] = {"a": 1}

# for 3.9 and later, you can use the built-in generic types:
nums1: list[int] = [1, 2, 3]
mapping1: dict[str, int] = {"a": 1}


def find_name(id: int) -> Optional[str]:
    if id == 1:
        return "Mohit"
    return None


def find_name_new_syntax(id: int) -> str | None:
    return "Mohit" if id == 1 else None




#union type hinting
def process(x: int | str) -> None:
    return None




#Any type hinting
def print_data(x: Any) -> None:
    print(x)
    



from typing import Callable
# using callable type hinting to specify a function that takes two integers and returns an integer
def apply_func(f: Callable[[int, int], int], a: int, b: int) -> int:
    return f(a, b)

def mul(a: int, b: int) -> int:
    return a * b

print(apply_func(mul, 2, 3))





# TypedDict

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def get_user() -> User:
    return {"name": "Mohit", "age": 21}




# DataClasses
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    
s = Student("Mohit", 21)



# Generics
from typing import TypeVar, List

T = TypeVar('T')

def first_element(arr: List[T]) -> T:
    return arr[0]





# final
from typing import Final

PI: Final = 3.14