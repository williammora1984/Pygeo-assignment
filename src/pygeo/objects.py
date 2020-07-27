import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    """A ray that is described by an initial point and a direction unit vector"""
    def __init__(self, I_point,D_vector):
        #I_point : Initial point (point)
        #D_vector : Direction vector (vector)
        self._I_point = np.array(I_point, dtype=float)
        self._D_vector = np.array(D_vector, dtype=float)/np.linalg.norm(D_vector)

    def __repr__(self):
        return f"Ray initial point({self._I_point.tolist()}),Ray unit vector({self._D_vector.tolist()})"

    def __eq__(self, other):
        if isinstance(other, Ray):
            return np.array_equal(other._I_point, self._I_point) and np.array_equal(other._D_vector, self._D_vector)
        return False


class Sphere:
    """A sphere."""
    """A sphere that is described by an center point and a radiusr"""
    def __init__(self, c_point,radius):
        self._c_point = np.array(c_point, dtype=float)
        self._radius = np.array(radius, dtype=float)

    def __repr__(self):
        return f"Center of sphere({self._c_point.tolist()}), radius of sphere({self._radius.tolist()})" 

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return np.array_equal(other._c_point, self._c_point) and np.array_equal(other._radius, self._radius)
        return False


class Triangle:
    ...
