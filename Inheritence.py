# Inheritance can be single , multi-level and mutliple
# Defination: Inheritance is a process of creating new class from existing class

# classes
class A:
    def function_of_A(self):
        print("This is class (A)")
class B:
    def function_of_B(self):
        print("This is class (B)")
class C(A,B):
    def function_of_C(self):
        print("This is class (C)")

# object
obj = C()
obj.function_of_A()
obj.function_of_B()
obj.function_of_C()
#end of code