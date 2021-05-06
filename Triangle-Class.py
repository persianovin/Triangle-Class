#import math

class Triangle:

    def __init__(self, a=1, b=1, t=90):
        import math
        global math
        self.a = a
        self.b = b
        self.t = math.radians(t)

    def third_side(self):
        return math.sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*math.cos(self.t))

    def circumference(self):
        return self.a + self.b + self.third_side()


a_side, b_side, theta = map(float, input('Enter dimensions: ').split())

shape = Triangle(a_side, b_side, theta)

print('--------result--------')
print(f'c side:         {round(shape.third_side(), 2)}')
print(f'Circumference:  {round(Triangle(a_side, b_side, theta).circumference(), 2)}')
print(f'a side:         {shape.a}')
print(f'b side:         {Triangle(a_side, b_side, theta).b}')
print(f'Theta(radians): {round(shape.t, 2)}')
