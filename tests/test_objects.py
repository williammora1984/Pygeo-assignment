from pygeo.objects import Point, Vector,Ray,Sphere

# Point.__eq__
def test__point_equal__given_two_equal_points__return_true():
    assert (Point((1, 2, 3)) == Point((1, 2, 3))) is True


def test__point_equal__given_two_not_equal_points__return_false():
    assert (Point((1, 2, 3)) == Point((4, 5, 6))) is False


# Vector.__eq__
def test__vector_equal__given_two_equal_vectors__return_true():
    assert (Vector((1, 2, 3)) == Vector((1, 2, 3))) is True


def test__vector_equal__given_two_not_equal_vectors__return_false():
    assert (Vector((1, 2, 3)) == Vector((4, 5, 6))) is False


# Point.__add__
def test__point_addition__given_point_and_vector__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Point((0, 1, 2)) + Vector((3, 4, 5)) == Point((3, 5, 7))


# Point.__radd__
def test__point_right_addition__given_vector_and_point__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Vector((0, 1, 2)) + Point((3, 4, 5)) == Point((3, 5, 7))


# Point.__sub__
def test__point_subtraction__given_two_points__return_correct_vector():
    """The result of a point being subtracted from another one is a vector."""
    assert Point((0, 1, 2)) - Point((3, 4, 5)) == Vector((-3, -3, -3))


# Vector.__add__
def test__vector_addition__given_two_vector__return_correct_vector():
    """The result of a vector being added to another one is a vector."""
    assert Vector((0, 1, 2)) + Vector((3, 4, 5)) == Vector((3, 5, 7))


# Vector.__sub__
def test__vector_subtraction__given_two_vectors__return_correct_vector():
    """The result of a vector being subtracted from another one is a vector."""
    assert Vector((0, 1, 2)) - Vector((3, 4, 5)) == Vector((-3, -3, -3))

## Ray.__eq__
def test_ray_eq_same_initial_point_and_same_direction__return_True():
    Ray1=Ray([1,1,1],[5,5,5])
    Ray2=Ray([1,1,1],[5,5,5])
    assert (Ray1==Ray2) is True

def test_ray_eq_same_initial_point_and_different_direction__return_False():
    Ray1=Ray([1,1,1],[5,5,5])
    Ray3=Ray([1,1,1],[1,5,1])
    assert ((Ray1==Ray3)) is False

def test_ray_eq_different_initial_point_and_same_direction__return_False():
    Ray3=Ray([1,1,1],[1,5,1])
    Ray4=Ray([2,2,2],[1,5,1])
    assert ((Ray3==Ray4)) is False

def test_ray_eq_different_initial_points_and_different_directions__return_False():
    Ray1=Ray([1,1,1],[5,5,5])
    Ray4=Ray([2,2,2],[1,5,1])
    assert ((Ray1==Ray4)) is False

# Sphere.__eq

def test_sphere_eq_same_center_point_and_same_radius__return_True():
    Sphere1=Sphere([1,1,1],5)
    Sphere2=Sphere([1,1,1],5)
    assert (Sphere1==Sphere2) is True

def test_sphere_eq_same_center_point_and_different_radius__return_False():
    Sphere1=Sphere([1,1,1],5)
    Sphere3=Sphere([1,1,1],7)
    assert (Sphere1==Sphere3) is False

def test_sphere_eq_different_center_point_and_same_radius__return_False():
    Sphere3=Sphere([1,1,1],7)
    Sphere4=Sphere([2,2,2],7)
    assert (Sphere3==Sphere4) is False

def test_sphere_eq_different_center_point_and_different_radius__return_False():
    Sphere1=Sphere([1,1,1],5)
    Sphere4=Sphere([2,2,2],7)
    assert (Sphere1==Sphere4) is False