

if __name__ == "__main__":
    from math import sqrt, pi, sin, cos, tan

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def vertices(self):
        pass


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def area(self):
        a = self.x1 * (self.y2 - self.y3)
        b = self.x2 * (self.y3 - self.y1)
        c = self.x3 * (self.y1 - self.y2)
        return abs(a + b + c) / 2

    def perimeter(self):
        d1 = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        d2 = sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        d3 = sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return d1 + d2 + d3

    def vertices(self):
        return 3


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height

    def perimeter(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return 2 * (width + height)

    def vertices(self):
        return 4


class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return pi * self.r * self.r

    def perimeter(self):
        return 2 * pi * self.r

    def vertices(self):
        return 0


class Polygon(Shape):
    def __init__(self, x, y, r, n):
        self.x = x
        self.y = y
        self.r = r
        self.n = n

    def area(self):
        return (self.n * self.r * self.r * sin(2 * pi / self.n)) / 2

    def perimeter(self):
        side = 2 * self.r * sin(pi / self.n)
        return self.n * side

    def vertices(self):
        return self.n


shapes = []

print("Доступные фигуры:")
print("triangle x1 y1 x2 y2 x3 y3")
print("rectangle x1 y1 x2 y2")
print("circle x y r")
print("polygon x y r n")
print("Команды:")
print("")
print("area - общая площадь")
print("perimeter - общий периметр")
print("vertices - всего вершин")
print("list - список фигур")
print("exit - выход")
print("")
print("Введите фигуры:")

while True:
    cmd = input("").strip()

    if cmd == "exit":
        break

    if cmd == "list":
        if not shapes:
            print("Нет фигур")
        for i, s in enumerate(shapes):
            print(f"{i + 1}. {type(s).__name__}")
        continue

    parts = cmd.split()
    if not parts:
        continue

    if parts[0] == "area":
        total = 0
        for s in shapes:
            total += s.area()
        print(f"Общая площадь: {total:.2f}")
        continue

    if parts[0] == "perimeter":
        total = 0
        for s in shapes:
            total += s.perimeter()
        print(f"Общий периметр: {total:.2f}")
        continue

    if parts[0] == "vertices":
        total = 0
        for s in shapes:
            total += s.vertices()
        print(f"Всего вершин: {total}")
        continue

    try:
        if parts[0] == "triangle":
            if len(parts) != 7:
                print("Нужно 6 чисел для треугольника")
                continue
            x1, y1, x2, y2, x3, y3 = map(float, parts[1:])
            t = Triangle(x1, y1, x2, y2, x3, y3)
            shapes.append(t)
            print("Треугольник добавлен")

        elif parts[0] == "rectangle":
            if len(parts) != 5:
                print("Нужно 4 числа для прямоугольника")
                continue
            x1, y1, x2, y2 = map(float, parts[1:])
            r = Rectangle(x1, y1, x2, y2)
            shapes.append(r)
            print("Прямоугольник добавлен")

        elif parts[0] == "circle":
            if len(parts) != 4:
                print("Нужно 3 числа для круга")
                continue
            x, y, r = map(float, parts[1:])
            if r <= 0:
                print("Радиус должен быть > 0")
                continue
            c = Circle(x, y, r)
            shapes.append(c)
            print("Круг добавлен")

        elif parts[0] == "polygon":
            if len(parts) != 5:
                print("Нужно 4 числа для многоугольника")
                continue
            x, y, r, n = map(float, parts[1:])
            if n < 3:
                print("Нужно минимум 3 стороны")
                continue
            if r <= 0:
                print("Радиус должен быть > 0")
                continue
            p = Polygon(x, y, r, int(n))
            shapes.append(p)
            print("Многоугольник добавлен")

        else:
            print("Неизвестная команда")

    except:
        print("Ошибка ввода")
