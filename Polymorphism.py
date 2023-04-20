# Polymorphism includes; over-riding and over-loading
# Over-riding ; After inheritance , if parent and child classes have same function name then child class will over-ride the function of parent class which has same name.So we use super() to make difference between them.
# Over-loading ; The same function name being used for different types by passing different arrguments.

# classes
class A:
    name = "Abdullah Khan"
    def fun(self):
        print("My name is (Abdullah Khan)")
class B(A):
    name = "Waseem Khan"
    def fun(self):
        print("My name is (Waseem Khan)")
        super().fun()

# object
obj = B()
print(obj.name)
print(obj.fun())

