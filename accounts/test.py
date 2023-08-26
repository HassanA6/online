
# create class 
class Test :

    def __new__(cls):
        self.x=9
        print("x is in the new dunder" sellf.x)
    def __init__(self):
        self.x=5

    def add(self):
        return self.x

a = Test()
print(a.add())

class Test2 :
    def __init__(self):
        self.x=4
    
    
        

# create object of class
t = Test2()

