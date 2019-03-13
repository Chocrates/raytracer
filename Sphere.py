from Tuple import *
from Matrix import *

class Sphere:
	def __init__(self,origin=Point(0,0,0)):
		self.origin = origin
		self.transform = Matrix.identity()

	def __eq__(self,other):
		return self.origin == other.origin

