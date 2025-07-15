import math

class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Vector must have at least one component.")
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize the zero vector.")
        return Vector(*(a / mag for a in self.components))
