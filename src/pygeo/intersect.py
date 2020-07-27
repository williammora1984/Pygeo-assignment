from .objects import Ray, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):

    if isinstance(ray, Ray) and isinstance(sphere,Sphere): #First it is verified that you are going to compute the intersection of the right elements 

        o_c=(ray._I_point-sphere._c_point)
        print("(np.dot(ray._D_vector,o_c))**2 : ",(np.dot(ray._D_vector,o_c))**2)
        nabla=(np.dot(ray._D_vector,o_c))**2-(np.dot(o_c,o_c)-sphere._radius**2)
        print("nabla", nabla)
        if nabla <0: #There is not intersection point
            print("option 1")
            return False
        elif nabla==0: #The Ray is tangent to the spehere, therefore the intersection is 1 point
            print("option 2")
            d=-np.dot(ray._D_vector,o_c)
            intersection=ray._I_point+ray._D_vector*d
        else: 
            """Nabla is bigger than 0, then there are two options, one itersection point
             or two intersections point, which depends on the value of d."""
            d=np.array([0,0]) 
            d[0]=-np.dot(ray._D_vector,o_c)+nabla**0.5
            d[1]=-np.dot(ray._D_vector,o_c)-nabla**0.5    
            if d[0]>0 and d[1]>0: #There are two intersection points, because the ray is out of the sphere
                print("option 3")
                intersection=([0,0])
                intersection[0]=(ray._I_point+ray._D_vector*d[0])
                intersection[1]=(ray._I_point+ray._D_vector*d[1])
                intersection=np.array(intersection,dtype=float)
            elif d[0]>0: 
                print("option 4")
                intersection=ray._I_point+ray._D_vector*d[0]
            else :
                print("option 5")
                intersection=ray._I_point+ray._D_vector*d[1]
        return intersection
    return False


def _intersect_ray_with_triangle(ray, triangle):
    ...