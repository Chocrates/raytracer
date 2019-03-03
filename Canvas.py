from Tuple import *
import copy

class Canvas:
	def __init__(self, width, height, default_color=Color(0,0,0)):
		self.width = width
		self.height = height
		self.pixels = self.generate_pixels(width,height, default_color)

	def generate_pixels(self,width,height,color):
		pixels = []
		for i in range(height):
			pixels.append([])
			for j in range(width):
				pixels[i].append(Pixel(i,j,copy.deepcopy(color)))
		return pixels

	def generate_ppm(self):
		ppm = ('P3\n'
			f'{self.width} {self.height}\n'
			'255\n')

		for row in self.pixels:
			row_str = ''
			first = True
			for col in row:
				clamped = col.clamp()
				row_str += ' ' if not first else ''
				red_str = f'{clamped[0]}'
				if len(row_str) + len(red_str) > 70:
					row_str += '\n'
					ppm += row_str
					row_str = red_str
				else:
					row_str += red_str
					
				green_str = f' {clamped[1]}'
				if len(row_str) + len(green_str) > 70:
					row_str += '\n'
					ppm += row_str
					row_str = f'{clamped[1]}' 
				else:
					row_str += green_str

				blue_str = f' {clamped[2]}'
				if len(row_str) + len(blue_str) > 70:
					row_str += '\n'
					ppm += row_str
					row_str = f'{clamped[2]}' 
				else:
					row_str += blue_str

				first = False
			row_str += '\n'
			ppm += row_str

		ppm += '\n'
		return ppm



class Pixel:
	def __init__(self,x,y,color):
		self.x = x
		self.y = y
		self.color = color

	def normalize(self,color):
		if color < 0:
			return 0
		elif color > 1:
			return 1
		else:
			return color

	def clamp(self):
		return (round(self.normalize(self.color.red)*255), 
			round(self.normalize(self.color.green)*255), 
			round(self.normalize(self.color.blue)*255))
