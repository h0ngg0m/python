## yield
```python
def g():
    for i in range(4):
        yield i
```
- 파이썬은 def 안에 yield 키워드를 사용하면 함수를 제너레이터로 취급한다.
- 따라서 g()를 호출하면 제너레이터 객체가 반환되고, 아무 코드도 실행되지 않는다.
```python
def g():
    for i in range(4):
        print('g')
        yield i

a = g() # 아무 코드도 실행되지 않는다.
```

## yield - 반복문
```python
def g():
    for i in range(4):
        print('g')
        yield i

a = g()

for i in a:
    print(i)
'''
g
0
g
1
g
2
g
3
'''
```
- return과 달리 yield는 함수를 종료하지 않고 yield가 실행된 시점을 기억하고 다음 반복 때는 yield 다음 코드부터 실행한다.

## yield - next()
```python
def g():
    for i in range(4):
        print('g')
        yield i

a = g()

print(next(a)) 
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
g
0
g
1
g
2
g
3
Traceback (most recent call last):
  File "/Users/honggom/Desktop/projects/python/test.py", line 12, in <module>
    print(next(a)) # StopIteration
          ^^^^^^^
StopIteration
'''
```
- next()를 호출하면 yield가 실행된 시점부터 다음 yield가 실행될 때까지 코드를 실행한다.
- yield가 실행되지 않은 상태에서 next()를 호출하면 StopIteration 예외가 발생한다.

## yield - 재사용
```python
def yield_3():
    yield 3
    yield 3.3
    yield 3.33

y3 = yield_3()

for i in y3:
    print(i)
'''
3
3.3
3.33
'''

for i in y3:
    print("second i = {}".format(i)) # nothing printed
```
- yield문을 전부 실행하고 다시 해당 generator를 호출하면 아무것도 출력되지 않는다.
- 다시 호출하려면 generator를 다시 만들어야 한다.
```python
new_y3 = yield_3()
print(next(new_y3))
print(next(new_y3))
print(next(new_y3))
'''
3
3.3
3.33
'''
```

