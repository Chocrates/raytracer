import math
from Intersection import *
import copy

class Ray:
	def __init__(self,origin,direction):
		self.origin = origin
		self.direction = direction
	
	def position(self,time):
		return self.origin + self.direction * time

	def intersects(self,other):
		sphere_to_ray = self.origin - other.origin
		a = self.direction.dot(self.direction)
		b = 2 * self.direction.dot(sphere_to_ray) 
		c = sphere_to_ray.dot(sphere_to_ray) - 1

		discriminant = b * b - 4 * a * c

		if discriminant < 0:
			return ()

		t1 = (-b - math.sqrt(discriminant))/(2*a)
		t2 = (-b + math.sqrt(discriminant))/(2*a)

		return (Intersection(t1,other),Intersection(t2,other))

	def transform(self,matrix):
		return Ray(matrix * copy.deepcopy(self.origin), matrix * copy.deepcopy(self.direction))

