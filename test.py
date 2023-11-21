class Parent:
    meta = "parent"

    @classmethod
    def class_method(cls):
        return cls()

    @staticmethod
    def static_method():
        return Parent()


class Child(Parent):
    meta = "child"


test1 = Child.class_method()
test2 = Child.static_method()

print(test1.meta) # child
print(test2.meta) # parent