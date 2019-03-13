
class Intersection:
	def __init__(self,t,shape):
		self.t = t
		self.shape = shape

class Intersections:
	def __init__(self,*args):
		self.data = list(args)

	def __len__(self):
		return len(self.data)
	
	def __getitem__(self, i):
		return self.data[i]

	def __iter__(self):
		return iter(self.data)

	def __next__(self):
		return next(self.data)
