## Closure

```python
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()

my_func() # Hi
print(my_func.__closure__[0].cell_contents) # Hi
```
1. 클로저 형성: outer_func이 호출될 때, inner_func 함수 객체가 생성되고 반환된다. 
이때 inner_func은 outer_func의 지역 변수 message에 대한 참조를 유지한다. 
이러한 함수와 그 함수의 둘러싼 환경(여기서는 message 변수를 포함하는 outer_func의 환경)을 클로저라고 한다.

2. 클로저의 사용: my_func = outer_func()는 outer_func를 호출하고, 결과로 inner_func 함수 객체를 my_func에 할당한다. 
이 시점에서 outer_func의 실행은 종료되었지만, inner_func은 여전히 message에 대한 참조를 유지한다.

3. my_func() 호출: my_func()를 호출하면, 이는 사실 inner_func()를 호출하는 것과 같다. 이 함수는 여전히 message에 접근할 수 있으므로 'Hi'를 출력한다.

4. 클로저의 내부 상태 접근: my_func.__closure__는 my_func (즉, inner_func)에 의해 캡처된 변수들을 포함하는 튜플이다. 
--closure--[0]는 첫 번째 캡처된 변수에 대한 정보를 담고 있고, cell_contents는 그 변수의 실제 값을 나타낸다. 이 경우 message의 값인 'Hi'를 출력한다.


## Decorator

```python
def deco(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper


@deco
def test(a, *, b, c):
    print(a, b, c)


test(1, b=2, c=3) # 이 함수는 보기에는 test 함수지만 사실 wrapper 함수이다.

print(test.__name__) # wrapper
'''
before
1 2 3
after
wrapper
'''

# 클래스 데코레이터
class Deco:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        self.func(*args, **kwargs)
        print("after")
```
- 클로저를 이용하여 함수를 감싸서 함수의 앞뒤에 코드를 추가할 수 있다.
- 데코레이터는 함수를 인자로 받아서 함수를 반환하는 함수이다.
- @deco는 test = deco(test)와 같다.

## Decorator with arguments

```python
def deco_with_args(decoargs):
    def deco(func):
        def wrapper(*args, **kwargs):
            print("before")
            print('decoargs', decoargs)
            func(*args, **kwargs)
            print("after")
        return wrapper
    return deco

@deco_with_args('decoargs')
def test(a, *, b, c):
    print(a, b, c)


test(1, b=2, c=3)
'''
before
decoargs decoargs
1 2 3
after
'''

# 클래스 데코레이터
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
```
- 데코레이터에 인자를 전달하려면 데코레이터를 반환하는 함수를 만들어야 한다.
- @deco_with_args('decoargs')는 test = deco_with_args('decoargs')(test)와 같다.
  - 내가 편하게 이해하고 있는 방법은 @deco_with_args('decoargs')가 호출되면 그 자리에 deco가 남는다고 생각하는 것이다.  