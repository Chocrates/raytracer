class Light:
	def __init__(self,position,intensity):
		self.position = position
		self.intensity = intensity

class PointLight(Light):
	def __init__(self,position,intensity):
		super().__init__(position,intensity)
