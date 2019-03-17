from Tuple import *
class Material:
	def __init__(self):
		self.ambient = 0.1
		self.diffuse = 0.9
		self.specular = 0.9
		self.shininess = 200.0
		self.color = Color(1,1,1)

	def __eq__(self,other):
		return self.ambient == other.ambient and \
			self.diffuse == other.diffuse and \
			self.specular == other.specular and \
			self.shininess == other.shininess and \
			self.color == other.color
