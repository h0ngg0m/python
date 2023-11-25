## with
```python
import time
class Timer:
    def __enter__(self):
        print('enter')
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(time.time() - self.start_time)

with Timer():
    print("in")
    time.sleep(1)
'''
enter
in
exit
1.006248950958252
'''
```
- with문을 사용하면 with문 내부의 코드가 실행되기 전에 __enter__가 실행되고, with문 내부의 코드가 모두 실행되고 나면 __exit__가 실행된다.


## with as
```python
import time
class Timer:
    def __init__(self, num):
        self.num = num
        
    def __enter__(self):
        print('enter')
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(time.time() - self.start_time)

    def func(self):
        print(self.num)

with Timer(10) as t:
    t.func()
    time.sleep(1)
```
- with as를 사용하면 __enter__에서 return한 값을 as 뒤의 변수에 할당할 수 있다.