from Tuple import *
from Matrix import *

class Sphere:
	def __init__(self,origin=Point(0,0,0)):
		self.origin = origin
		self.transform = Matrix.identity()

	def __eq__(self,other):
		return self.origin == other.origin

	def normal(self,world_point):
		print(f'WorldPoint: {world_point}')
		print(f'Sphere: {self.transform.data}')
		object_point = self.transform.inverse() * world_point
		print(f'ObjectPoint: {object_point}')
		object_normal = object_point - Point(0,0,0)
		world_normal = self.transform.inverse().transpose() * object_normal
		world_normal.w = 0
		print(f'Normal: {world_normal}')
		print(f'Normal: {world_normal.normalize()}')
		return world_normal.normalize()
