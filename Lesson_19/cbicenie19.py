# dekorátor, wrapper
import time

def my_decorator(func):
    def wrapper():
        print("Something before---")
        func()
        print("Something after---")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

@my_decorator
def mocnina():
    print(2*2)

say_hello()
mocnina()

# PRIKLAD 2
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcia {func.__name__} vykonaná za {end_time - start_time: } sekund")
        return result
    return wrapper

@timing_decorator
def pomala_funkcia():
    time.sleep(2)
    print("Pomaly vykonaná funkcia")

@timing_decorator
def rychla_funkcia():
    time.sleep(1)
    print("Rychle vykonaná funkcia")



pomala_funkcia()
rychla_funkcia()
