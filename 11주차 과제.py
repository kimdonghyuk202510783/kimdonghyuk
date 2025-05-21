

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.lt = Point(x1, y1)  
        self.rb = Point(x2, y2)  

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.lt.getX()},{self.lt.getY()})이고 , 우측 하단 꼭지점이 ({self.rb.getX()},{self.rb.getY()})인 사각형 입니다')

    def getWidth(self):
        return self.rb.getX() - self.lt.getX()

    def getHeight(self):
        return self.rb.getY() - self.lt.getY()

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())





r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')








    
