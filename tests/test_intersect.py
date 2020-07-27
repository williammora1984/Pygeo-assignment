from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle
import numpy as np

# intersect


# _intersect_ray_with_sphere

def test_intersect_ray_sphere_no_intersect__return_False():
    Ray1=Ray((0,0,6),(1,0,0))
    Sphere1=Sphere((0,0,0),5)
    assert _intersect_ray_with_sphere(Ray1, Sphere1) is False

def test_intersect_ray_sphere_one_intersect__one_correct_point():
    Ray1=Ray((0,0,0),(1,0,0))
    Sphere1=Sphere((0,0,0),5)
    np.testing.assert_array_equal (_intersect_ray_with_sphere(Ray1, Sphere1),np.array([5,0,0]))

def test_intersect_ray_sphere_one_intersect_tangent_point__one_correct_point():
    Ray1=Ray((5,5,0),(0,0,1))
    Sphere1=Sphere((5,5,0),5)
    np.testing.assert_array_equal (_intersect_ray_with_sphere(Ray1, Sphere1),np.array([5,5,5]))

def test_intersect_ray_sphere_two_intersect_horizontal__two_correct_points():
    Ray1=Ray((-6,0,0),[1,0,0])
    Sphere1=Sphere((0,0,0),5)
    np.testing.assert_array_equal (_intersect_ray_with_sphere(Ray1, Sphere1),np.array([[5.0,0,0],[-5.0,0,0]])) 
    
def test_intersect_ray_sphere_two_intersect_vertical__two_correct_points():
    Ray1=Ray((1,0,0),[0,1,0])
    Sphere1=Sphere((1,6,0),5)
    np.testing.assert_array_equal (_intersect_ray_with_sphere(Ray1, Sphere1),np.array([[1.0,11.0,0],[1.0,1.0,0]])) 
