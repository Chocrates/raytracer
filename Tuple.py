import math
class Tuple:
	def __init__(self, x,y,z,w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
	
	def __eq__(self, other):
		return all(map(lambda x: math.fabs(x[0] - x[1] < x[2]), [l + [1e-4] for l in [[self.x,other.x],[self.y,other.y],[self.z,other.z],[self.w,other.w]]]))
	
	def __add__(self, other):
		return Tuple(self.x + other.x,
			self.y + other.y,
			self.z + other.z,
			self.w + other.w)
	
	def __sub__(self,other):
		return Tuple(self.x - other.x,
			self.y - other.y,
			self.z - other.z,
			self.w - other.w)
	
	def __neg__(self):
		return Tuple(-self.x,
			-self.y,
			-self.z,
			-self.w)

	def __mul__(self,right):
		if isinstance(right,Tuple):
			return Tuple(self.x * right.x,
				self.y * right.y,
				self.z * right.z,
				self.w * right.w)
		else:
			return Tuple(self.x * right,
				self.y * right,
				self.z * right,
				self.w * right)

	def __truediv__(self, scalar):
		return Tuple(self.x / scalar,
			self.y / scalar,
			self.z / scalar,
			self.w / scalar)
	
	def __repr__(self):
		return f'Tuple({self.x},{self.y},{self.z},{self.w})'

	@property
	def magnitude(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
	
	def normalize(self):
		mag = self.magnitude
		return Tuple(self.x/mag,
			self.y/mag,
			self.z/mag,
			self.w/mag)
	def dot(self,other):
		return self.x * other.x + \
			self.y * other.y + \
			self.z * other.z + \
			self.w * other.w 
	
	def cross(self,other):
		return Vector(self.y * other.z - self.z * other.y,
			self.z * other.x - self.x * other.z,
			self.x * other.y - self.y * other.x)

class Point(Tuple):
	def __init__(self,x,y,z):
		super(Point,self).__init__(x,y,z,1.0)	

class Vector(Tuple):
	def __init__(self,x,y,z):
		super(Vector,self).__init__(x,y,z,0.0)
	
	def reflect(self,other):
		return self - other * 2 * self.dot(other)

class Color(Tuple):
	def __init__(self,r,g,b):
		super(Color,self).__init__(r,g,b,0.0)
	
	@property
	def red(self):
		return self.x

	@property
	def green(self):
		return self.y

	@property
	def blue(self):
		return self.z
