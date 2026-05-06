from typing import Optional, Literal, Generic, TypeVar
from enum import Enum

from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ValidationError,
)


# python typing is only for IDE and improve the developer experience,
# it does not enforce type checking at runtime. So the solution is pydantic which is a 
# data validation library that uses python type hints to validate the data at runtime. 

# I Learned about pydantic which is used to data validation and auto conversion of data types.
# It is very useful when we are working with APIs and we want to validate the 
# data coming from the client. 

# I learned about BaseModel , field, EmailStr, ValidationError, Literal and Enum from pydantic.


name: str = "Mohit"
age: int = 21
height: float = 5.9
is_student: bool = True

print(name)
print(age)
print(height)
print(is_student)





class User(BaseModel):
    name: str
    age: int


user = User(name="Mohit", age=21)

print(user)

# Pydantic auto converts string -> int
user2 = User(name="Rahul", age="25")

print(user2)
print(type(user2.age))



# VALIDATION ERROR


try:
    User(name="Test", age="abc")

except ValidationError as e:
    print(e)


# OPTIONAL FIELDS
class Student(BaseModel):
    name: str
    phone: Optional[str] = None


s1 = Student(name="Mohit")
s2 = Student(name="Rahul", phone="9999999999")

print(s1)
print(s2)


# DEFAULT VALUES

class Product(BaseModel):
    title: str
    in_stock: bool = True


p1 = Product(title="Laptop")

print(p1)



# NESTED MODELS

class Address(BaseModel):
    city: str
    state: str
    pincode: str


class Customer(BaseModel):
    name: str
    address: Address


customer = Customer(
    name="Mohit",
    address=Address(
        city="hello",
        state="odisha",
        pincode="761206"
        )
)

print(customer)

print(customer.address.city)


# LIST TYPES

class Cart(BaseModel):
    items: list[str]


cart = Cart(items=["Laptop", "Mouse", "Keyboard"])

print(cart)



# LIST OF MODELS


class Item(BaseModel):
    title: str
    price: float


class Order(BaseModel):
    items: list[Item]


order = Order(
    items=[
        {
            "title": "Laptop",
            "price": 50000
        },
        {
            "title": "Mouse",
            "price": 500
        }
    ]
)

print(order)




print("\n========== FIELD VALIDATIONS ==========\n")


class Employee(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    salary: float = Field(gt=0)
    age: int = Field(ge=18)


emp = Employee(
    name="Mohit",
    salary=50000,
    age=21
)

print(emp)


# =========================================================
# EMAIL VALIDATION
# =========================================================

print("\n========== EMAIL VALIDATION ==========\n")


class Account(BaseModel):
    email: EmailStr


acc = Account(email="mohit@gmail.com")

print(acc)


# =========================================================
# LITERAL
# =========================================================

print("\n========== LITERAL ==========\n")


class Payment(BaseModel):
    amount: float
    status: Literal["pending", "success", "failed"]


payment = Payment(
    amount=1000,
    status="success"
)

print(payment)


# =========================================================
# ENUM
# =========================================================

print("\n========== ENUM ==========\n")


class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"


class Shipment(BaseModel):
    tracking_id: str
    status: OrderStatus


shipment = Shipment(
    tracking_id="TRK123",
    status=OrderStatus.shipped
)

print(shipment)

