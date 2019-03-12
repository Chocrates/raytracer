from Tuple import *
from Translation import *
import re

@given('{attr:w} translation({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Translation(x,y,z))

@then('{attr1:w} * {attr2:w} = point({x:S},{y:S},{z:S})')
def step_impl(context,attr1,attr2,x,y,z):
	x_num = parse_math_string(x)
	y_num = parse_math_string(y)
	z_num = parse_math_string(z)
	t = getattr(context,attr1)
	p = getattr(context,attr2)

	print(f'X: {x_num}, Y: {y_num}, Z: {z_num}')
	print(f'Point: {Point(x_num,y_num,z_num)}')
	assert t * p == Point(x_num,y_num,z_num)

@then('{attr1:w} * {attr2:w} = point({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	t = getattr(context,attr1)
	p = getattr(context,attr2)
	assert t * p == Point(x,y,z)

@then('{attr1:w} * {attr2:w} = {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	c = getattr(context,attr3)
	assert a * b == c

@given('{attr:w} scaling({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Scaling(x,y,z))

@then('{attr1:w} * {attr2:w} = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a * b == Vector(x,y,z)

@given('{attr:w} rotation_{axis:w}({rad:S})')
def step_impl(context,attr,axis,rad):
	if axis == 'x':
		rot_axis = Rotation.Axis.X
	elif axis == 'y':
		rot_axis = Rotation.Axis.Y
	elif axis == 'z':
		rot_axis = Rotation.Axis.Z
	setattr(context,attr,Rotation(rot_axis,parse_math_string(rad)))

@given('{attr:w} shearing({x_y:g},{x_z:g},{y_x:g},{y_z:g},{z_x:g},{z_y:g})')
def step_impl(context,attr,x_y,x_z,y_x,y_z,z_x,z_y):
	print(f'Shearing: {Shearing(x_y,x_z,y_x,y_z,z_x,z_y).data}')
	setattr(context,attr,Shearing(x_y,x_z,y_x,y_z,z_x,z_y))

@when('{attr1:w} {attr2:w} * {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1, a * b)

@when('{attr1:w} {attr2:w} * {attr3:w} * {attr4:w}')
def step_impl(context,attr1,attr2,attr3,attr4):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	c = getattr(context,attr4)
	setattr(context,attr1, a * b * c)

@then('{attr:w} = point({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	a = getattr(context,attr)
	assert a == Point(x,y,z)

def parse_math_string(num_string):
	""" Parses square root, pi, and e in a number into a python representation """
	num_string = re.sub(r'√(\d+)', r'math.sqrt(\1)',num_string)
	num_string = re.sub(r'π', r'math.pi',num_string)
	num_string = re.sub(r'e', r'math.e',num_string)
	ns = {}
	exec(f'import math; out = {num_string}', {} , ns)
	return ns['out']

