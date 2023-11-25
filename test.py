class DecoWithArgs:
    def __init__(self, decoargs):
        self.decoargs = decoargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("before")
            print('decoargs', self.decoargs)
            result = func(*args, **kwargs)
            print("after")
            return result
        return wrapper


@DecoWithArgs("decoargs")
def test(a, *, b, c):
    print(a, b, c)


test(1, b=2, c=3)