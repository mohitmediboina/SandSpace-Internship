"""
========================================================
PYTHON DECORATORS PRACTICE FILE
========================================================

Topics:
1. Basic Decorator
2. functools.wraps
3. Decorator With Arguments
4. Multiple Decorators
5. Timing Decorator
6. Authentication Decorator
7. Retry Decorator
8. Memoization
9. Built-in Decorators
10. Class Decorator
11. Class Based Decorator
12. Async Decorator

========================================================
"""

from functools import wraps
import time
import asyncio


# ======================================================
# 1. BASIC DECORATOR
# ======================================================

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Running: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Finished: {func.__name__}")

        return result

    return wrapper


@logger
def hello():
    print("Hello World")


hello()


# ======================================================
# 2. DECORATOR WITH ARGUMENTS
# ======================================================

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for i in range(times):
                print(f"Repeat Count: {i+1}")

                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello {name}")


greet("Mohit")


# ======================================================
# 3. TIMING DECORATOR
# ======================================================

def calculate_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end - start:.4f} sec")

        return result

    return wrapper


@calculate_time
def heavy_task():

    time.sleep(2)

    print("Heavy Task Completed")


heavy_task()


# ======================================================
# 4. AUTH DECORATOR
# ======================================================

is_logged_in = True


def require_login(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not is_logged_in:
            raise Exception("Unauthorized")

        return func(*args, **kwargs)

    return wrapper


@require_login
def dashboard():
    print("Welcome Dashboard")


dashboard()


# ======================================================
# 5. RETRY DECORATOR
# ======================================================

def retry(max_retries):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(max_retries):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    print(f"Retry {attempt + 1} Failed")

                    time.sleep(1)

            raise Exception("All Retries Failed")

        return wrapper

    return decorator


counter = 0


@retry(3)
def unstable_api():

    global counter

    counter += 1

    if counter < 3:
        raise Exception("API Failed")

    return "Success"


print(unstable_api())


# ======================================================
# 6. MEMOIZATION DECORATOR
# ======================================================

def memoize(func):

    cache = {}

    @wraps(func)
    def wrapper(n):

        if n in cache:
            print("Cache Hit")
            return cache[n]

        print("Cache Miss")

        result = func(n)

        cache[n] = result

        return result

    return wrapper


@memoize
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# ======================================================
# 7. MULTIPLE DECORATORS
# ======================================================

def bold(func):

    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def italic(func):

    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


@bold
@italic
def text():
    return "Python"


print(text())


# ======================================================
# 8. STATICMETHOD / CLASSMETHOD / PROPERTY
# ======================================================

class User:

    total_users = 0

    def __init__(self, name, age):

        self._name = name
        self._age = age

        User.total_users += 1

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


u1 = User("Mohit", 21)

print(User.add(10, 20))

print(User.get_total_users())

print(u1.age)

u1.age = 25

print(u1.age)


# ======================================================
# 9. CLASS DECORATOR
# ======================================================

def add_methods(cls):

    def greet(self):
        return f"Hello {self.name}"

    cls.greet = greet

    return cls


@add_methods
class Person:

    def __init__(self, name):
        self.name = name


p = Person("Mohit")

print(p.greet())


# ======================================================
# 10. CLASS BASED DECORATOR
# ======================================================

class LoggerDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        print("Decorator Started")

        result = self.func(*args, **kwargs)

        print("Decorator Ended")

        return result


@LoggerDecorator
def test():
    print("Testing...")


test()


# ======================================================
# 11. ASYNC DECORATOR
# ======================================================

def async_logger(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):

        print("Async Function Started")

        result = await func(*args, **kwargs)

        print("Async Function Finished")

        return result

    return wrapper


@async_logger
async def fetch_data():

    await asyncio.sleep(1)

    return {"data": "success"}


async def main():

    result = await fetch_data()

    print(result)


asyncio.run(main())


# ======================================================
# END
# ======================================================