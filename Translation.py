from Matrix import *
from enum import Enum

class Transformation:
	def __init__(self):
		pass
	

class Translation(Matrix):
	def __init__(self,x,y,z):
		mat = Matrix.identity().data
		mat[0][3] = x
		mat[1][3] = y
		mat[2][3] = z
		self.data = mat

class Scaling(Matrix):
	def __init__(self,x,y,z):
		mat = Matrix.identity().data
		mat[0][0] = x
		mat[1][1] = y
		mat[2][2] = z
		self.data = mat

class Rotation(Matrix):
	class Axis(Enum):
		X = 0
		Y = 1
		Z = 2

	def __init__(self,axis,r):
		if axis == self.Axis.X:
			mat = Matrix.identity().data
			mat[1][1] = math.cos(r)
			mat[1][2] = -math.sin(r)
			mat[2][1] = math.sin(r)
			mat[2][2] = math.cos(r)
			self.data = mat
		elif axis == self.Axis.Y:
			mat = Matrix.identity().data
			mat[0][0] = math.cos(r)
			mat[0][2] = math.sin(r)
			mat[2][0] = -math.sin(r)
			mat[2][2] = math.cos(r)
			self.data = mat
		elif axis == self.Axis.Z:
			mat = Matrix.identity().data
			mat[0][0] = math.cos(r)
			mat[0][1] = -math.sin(r)
			mat[1][1] = math.sin(r)
			mat[1][2] = math.cos(r)
			self.data = mat

class Shearing(Matrix):
	def __init__(self,x_y,x_z,y_x,y_z,z_x,z_y):
		mat = Matrix.identity().data
		mat[0][1] = x_y
		mat[0][2] = x_z
		mat[1][0] = y_x
		mat[1][2] = y_z
		mat[2][0] = z_x
		mat[2][1] = z_y
		self.data = mat
