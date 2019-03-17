from behave import *
from Tuple import *
from Translation import *
import re
from Matrix import *
import math
from Ray import *
from Sphere import *
import importlib
from Canvas import *
import copy

def parse_math_string(num_string):
	""" Parses square root, pi, and e in a number into a python representation """
	num_string = re.sub(r'√(\d+)', r'math.sqrt(\1)',num_string)
	num_string = re.sub(r'π', r'math.pi',num_string)
	num_string = re.sub(r'e', r'math.e',num_string)
	ns = {}
	exec(f'import math; out = {num_string}', {} , ns)
	return ns['out']

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

@when('{attr1:w} ray({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,Ray(a,b))

@when('{attr1:w} transform({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,a.transform(b))

@when('{attr1:w} intersects({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,b.intersects(a))

@given('set_transform({attr1:w},{attr2:w})')
@when('set_transform({attr1:w},{attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	a.transform = b

@given('set_transform({attr:w},{method:w}({x:g},{y:g},{z:g}))')
@when('set_transform({attr:w},{method:w}({x:g},{y:g},{z:g}))')
def step_impl(context,attr,method,x,y,z):
	a = getattr(context,attr)
	# Extra hacky, capitalize the first char for the class name
	transform = getattr(importlib.import_module('Translation'),method.capitalize())
	a.transform = transform(x,y,z)

@when('{attr1:w} normal_at({attr2:w},point({x:S},{y:S},{z:S}))')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr2)
	xd = parse_math_string(x)
	yd = parse_math_string(y)
	zd = parse_math_string(z)
	setattr(context,attr1,a.normal(Point(xd,yd,zd)))

@when('every pixel of {attr} is color({r:g},{g:g},{b:g})')
def step_impl(context,attr,r,g,b):
	c = Color(r,g,b)
	canvas = getattr(context,attr)
	for i in canvas.pixels:
		for j in i:
			j.color = copy.deepcopy(c)

@when('write_pixel({canvas},{x:d},{y:d},{color})')
def step_impl(context,canvas,x,y,color):
	canvas = getattr(context,canvas)
	clr = getattr(context,color)
	canvas.pixels[y][x].color = clr

@when('{attr} canvas_to_ppm({canvas})')
def step_impl(context,attr,canvas):
	c = getattr(context,canvas)
	setattr(context,attr,c.generate_ppm())

@when('{attr1} = normalize({attr2})')
def step_impl(context,attr1,attr2):
	v = getattr(context,attr2)
	setattr(context,attr1,v.normalize())

@when('{attr1:w} hit({attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr2)
	setattr(context,attr1,a.hit())

@when('{attr1:w} reflect({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,a.reflect(b))

@when('{attr1:w}.{prop:w} {attr2:w}')
def step_impl(context,attr1,prop,attr2):
	a = getattr(context,attr1)
	b = getattr(a,prop)
	c = getattr(context,attr2)
	b = c

@when('{attr1:w} {attr2:w}.{prop:w}')
def step_impl(context,attr1,attr2,prop):
	a = getattr(context,attr2)
	b = getattr(a,prop)
	setattr(context,attr1,b)
