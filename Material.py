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

	def lighting(self,light,point,eyev,normalv):
		effective_color = self.color * light.intensity
		lightv = (light.position - point).normalize()
		ambient = effective_color * self.ambient
		light_dot_normal = lightv.dot(normalv)
		if light_dot_normal < 0:
			diffuse = Color(0,0,0)
			specular = Color(0,0,0)
		else:
			diffuse = effective_color * self.diffuse * light_dot_normal
			reflectv = (-lightv).reflect(normalv)
			reflect_dot_eye = reflectv.dot(eyev)
			if reflect_dot_eye <= 0:
				specular = Color(0,0,0)
			else:
				factor = math.pow(reflect_dot_eye, self.shininess)
				specular = light.intensity * self.specular * factor

		return ambient + diffuse + specular
