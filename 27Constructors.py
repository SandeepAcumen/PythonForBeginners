class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point =Point(10,20)
print(point.x)

#Example 2

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


john=Person("sandeep kumar")  
print(john.name) 
john.talk()

