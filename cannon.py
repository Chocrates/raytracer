from Tuple import *
from Canvas import *

projectile = type('',(object,),{})()
projectile.position = Point(0,1,0)
projectile.velocity = Vector(1,1,0).normalize() * 5

environment = type('',(object,),{})()
environment.gravity = Vector(0,-0.1,0)
environment.wind = Vector(-.01,0,0)

def tick(environment,projectile):
	pos = projectile.position + projectile.velocity
	velocity = projectile.velocity + environment.gravity + environment.wind
	new_proj = type('',(object,),{})()
	new_proj.position = pos
	new_proj.velocity = velocity
	return new_proj

if __name__ == '__main__':
	canvas = Canvas(100,50,Color(0,0,0))
	green = Color(0,1,0)
	print('Firing....')
	counter = 0
	while projectile.position.y > 0.0:
		counter += 1
		projectile = tick(environment,projectile)
		x = round(projectile.position.x)
		y = round(projectile.position.y)
		if canvas.height - y < canvas.height \
			and canvas.height - y > 0 \
			and x < canvas.width:
			canvas.pixels[canvas.height-y][x].color = green
		with open('cannon.ppm','w') as f:
			f.write(canvas.generate_ppm())
		print(projectile.position)
#		import pdb; pdb.set_trace()
		print(f'Canvas Height: {canvas.height}, Y: {y}, {canvas.height - y}, X: {x}, Canvas Width: {canvas.width}')

	print(f'Ticks: {counter}')

	with open('cannon.ppm','w') as f:
		f.write(canvas.generate_ppm())
