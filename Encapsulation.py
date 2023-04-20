# Encapsulation 
# In encapsulation we make private variables by using double underscore (__) which can be accessed only inside that class.

class A:
    __name = "Abdullah Khan Kakar"
    def __init__(self,name,font):
        self.__name = name
        self._font = font
        print(self.__name)
        print(self._font)
    
    def set_font(self, value):
        self._font = value
    
    def get_font(self):
        return self._font

        


obj = A("Waseem",23)
print(obj.get_font())
obj.set_font(26)
print(obj.get_font())

