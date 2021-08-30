print("Task 1")

print(list(filter(lambda x: x < 20, [1, 3, 2, 5, 20, 21])))

print("Task 3")

class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self, a):
        print('> до вызова из класса...', self.func.__name__)
        self.func(a)
        print('> после вызова из класса')

@Decorator
def wrapped(a):
    print('функція wrapped:', a**2)
    
def _wrapped(b):
    print('функція wrapped:', b**2)

print('>> старт')
wrapped(2)
_wrapped(3)
print('>> кінець')