
import random
import math
from itertools import combinations

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f"Triangle: {self.p1}, {self.p2}, {self.p3}"

    def perimeter(self) -> float:
        return (self.p1.distance_to(self.p2) +
                self.p2.distance_to(self.p3) +
                self.p3.distance_to(self.p1))

    def area(self) -> float:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def triangle_type(self) -> str:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)

        def almost_equal(x, y):
            return abs(x - y) < 0.01

        if almost_equal(a, b) and almost_equal(b, c):
            return "Рівносторонній"
        elif almost_equal(a, b) or almost_equal(b, c) or almost_equal(c, a):
            return "Рівнобедрений"
        else:
            return "Різносторонній"


class TriangleData:
    def __init__(self, points: list[Point]):
        self.points = points
        self.triangles = self._generate_valid_triangles()

    def _is_valid_triangle(self, p1: Point, p2: Point, p3: Point) -> bool:
        
        return (p2.x - p1.x) * (p3.y - p1.y) != (p2.y - p1.y) * (p3.x - p1.x)

    def _generate_valid_triangles(self):
        valid = []
        for p1, p2, p3 in combinations(self.points, 3):
            if self._is_valid_triangle(p1, p2, p3):
                valid.append(Triangle(p1, p2, p3))
        return valid

    def count_triangles(self):
        return len(self.triangles)

    def get_largest_triangle(self):
        return max(self.triangles, key=lambda t: t.area(), default=None)

    def get_smallest_triangle(self):
        return min(self.triangles, key=lambda t: t.area(), default=None)

    def get_triangles_by_type(self):
        stats = {"Рівносторонній": 0, "Рівнобедрений": 0, "Різносторонній": 0}
        for triangle in self.triangles:
            t_type = triangle.triangle_type()
            stats[t_type] += 1
        return stats


def generate_unique_points(n: int, min_val: int = -10, max_val: int = 10) -> list[Point]:
    seen = set()
    points = []
    while len(points) < n:
        x, y = random.randint(min_val, max_val), random.randint(min_val, max_val)
        if (x, y) not in seen:
            seen.add((x, y))
            points.append(Point(x, y))
    return points



if __name__ == "__main__":
    random.seed(1)  # Для стабільності результатів
    num_points = 20
    points = generate_unique_points(num_points)
    triangle_data = TriangleData(points)

    print(f"Кількість згенерованих точок: {num_points}")
    print(f"Кількість можливих трикутників: {triangle_data.count_triangles()}")

    largest = triangle_data.get_largest_triangle()
    if largest:
        print(f"\nНайбільший трикутник:\n{largest}\nПлоща: {largest.area():.2f}, Периметр: {largest.perimeter():.2f}")

    smallest = triangle_data.get_smallest_triangle()
    if smallest:
        print(f"\nНайменший трикутник:\n{smallest}\nПлоща: {smallest.area():.2f}, Периметр: {smallest.perimeter():.2f}")

    type_stats = triangle_data.get_triangles_by_type()
    print("\nСтатистика за типами трикутників:")
    for t_type, count in type_stats.items():
        print(f"{t_type}: {count}")









