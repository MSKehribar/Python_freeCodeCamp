class Rectangle:
    def __init__(self, gen, yuk):
        self.gen=gen
        self.yuk=yuk

    def __repr__(self):
        print("width=",self.gen,"height=",self.yuk)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.gen,self.yuk)

    def set_width(self, gen):
        self.gen=gen

    def set_height(self, yuk):
        self.yuk=yuk

    def get_area(self):
        return (self.gen * self.yuk)

    def get_perimeter(self):
        return (2 * self.gen + 2 * self.yuk)

    def get_diagonal(self): 
        return ((self.gen ** 2 + self.yuk ** 2) ** .5)

    def get_picture(self):
        p=''
        for i in range(self.yuk):
            p+='*'*self.gen+'\n'
        return p

    def get_amount_inside(self, rect):
        return (self.gen/rect.gen)*(self.yuk/rect.yuk)

class Square(Rectangle):
    def __init__(self, gen, yuk=[]):
        self.gen=gen
        self.yuk=gen


    def set_side(self,kenar):
        self.gen=kenar
        self.yuk=kenar

    def __str__(self):
        return "Square (Side={})".format(self.gen)



print("\n"*10)
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
