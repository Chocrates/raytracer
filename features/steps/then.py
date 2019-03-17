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
from Intersection import *

def parse_math_string(num_string):
	""" Parses square root, pi, and e in a number into a python representation """
	num_string = re.sub(r'√(\d+)', r'math.sqrt(\1)',num_string)
	num_string = re.sub(r'π', r'math.pi',num_string)
	num_string = re.sub(r'e', r'math.e',num_string)
	ns = {}
	exec(f'import math; out = {num_string}', {} , ns)
	return ns['out']


@then('{attr:w}[{x:d},{y:d}] = {num:g}')
def step_impl(context,attr,x,y,num):
	m = getattr(context,attr)
	assert math.isclose(m.data[x][y],num,rel_tol=1e-10)

@then('{attr:w}[{x:d},{y:d}] = {numerator:d}/{denominator:d}')
def step_impl(context,attr,x,y,numerator,denominator):
	m = getattr(context,attr)
	assert math.isclose(m.data[x][y],numerator/denominator,rel_tol=1e-10)

@then('{attr:w}.{prop:w} = identity_matrix')
def step_impl(context,attr,prop):
	a = getattr(context,attr)
	b = getattr(a,prop)
	assert b == Matrix.identity()

@then('{attr} = identity_matrix')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a == Matrix.identity()

@then('{attr1:w} = {attr2:w}')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a == b


@then('{attr1:w} != {attr2:w}')
def step_impl(context,attr1, attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a != b

@then('{attr1:w} * {attr2:w} is the following {x:g}x{y:g} matrix')
def step_impl(context,attr1,attr2,x,y):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	c = Matrix.build_matrix(context.text)
	assert a * b == c

@then('{attr1:w} * {attr2:w} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr1,attr2,x,y,z,w):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a * b == Tuple(x,y,z,w)

@then('{attr1:w} * identity_matrix = {attr2:w}')
def step_impl(context,attr1,attr2):
	attr1 = getattr(context,attr1)
	attr2 = getattr(context,attr2)
	assert attr1 * attr1.identity() == attr2

@then('identity_matrix * {attr1:w} = {attr2:w}')
def step_impl(context,attr1,attr2):
	attr1 = getattr(context,attr1)
	attr2 = getattr(context,attr2)
	assert Matrix.identity() * attr1 == attr2

@then('transpose({attr:w}) is the following matrix')
def step_impl(context,attr):
	a = getattr(context,attr)
	mat = Matrix.build_matrix(context.text)
	assert a.transpose() == mat

@then('determinant({attr:w}) = {num:g}')
def step_impl(context,attr,num):
	a = getattr(context,attr)
	assert a.determinant() == num

@then('submatrix({attr:w},{row:d},{col:d}) is the following {x:g}x{y:g} matrix')
def step_impl(context,attr,row,col,x,y):
	a = getattr(context,attr)
	assert a.submatrix(row,col) == Matrix.build_matrix(context.text)

@then('minor({attr:w},{row:d},{col:d}) = {num:g}')
def step_impl(context,attr,row,col,num):
	a = getattr(context,attr)
	assert a.minor(row,col) == num

@then('cofactor({attr:w},{row:d},{col:d}) = {num:g}')
def step_impl(context,attr,row,col,num):
	a = getattr(context,attr)
	assert a.cofactor(row,col) == num

@then('{attr:w} is invertible')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a.invertible == True

@then('{attr:w} is not invertible')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a.invertible == False

@then('{attr:w} is the following {x:d}x{y:d} matrix')
def step_impl(context,attr,x,y):
	a = getattr(context,attr)
	assert a == Matrix.build_matrix(context.text)

@then('inverse({attr:w}) is the following {x:d}x{y:d} matrix')
def step_impl(context,attr,x,y):
	a = getattr(context,attr)
	assert a.inverse() == Matrix.build_matrix(context.text)

@then('{attr1:w} * inverse({attr2:w}) = {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	c = getattr(context,attr3)
	assert a * b.inverse() == c

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

@then('{attr1:w} * {attr2:w} = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a * b == Vector(x,y,z)

@then('{attr:w} = point({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	a = getattr(context,attr)
	assert a == Point(x,y,z)

@then('{attr:w}.count = {num:g}')
def step_impl(context,attr,num):
    a = getattr(context,attr)
    assert len(a) == num

@then('position({ray:w},{t:g}) = point({x:g},{y:g},{z:g})')
def step_impl(context,ray,t,x,y,z):
	r = getattr(context,ray)
	assert r.position(t) == Point(x,y,z)

@then('{attr:w}.{prop:w} = point({x:g},{y:g},{z:g})')
def step_impl(context,attr,prop,x,y,z):
	a = getattr(context,attr)
	b = getattr(a,prop)
	assert b == Point(x,y,z)

@then('{attr:w}.{prop:w} = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr,prop,x,y,z):
	a = getattr(context,attr)
	b = getattr(a,prop)
	assert b == Vector(x,y,z)

@then('{attr1:w}[{idx:d}].{attr2:w} = {val:g}')
def step_impl(context,attr1,idx,attr2,val):
	a = getattr(context,attr1)
	b = getattr(a[idx],attr2)
	assert b == val

@then('{attr1:w}[{idx:d}].{attr2:w} = {val:w}')
def step_impl(context,attr1,idx,attr2,val):
	a = getattr(context,attr1)
	b = getattr(a[idx],attr2)
	c = getattr(context,val)
	assert b == c

@then('{attr:w} = vector({x:S},{y:S},{z:S})')
def step_impl(context,attr,x,y,z):
	a = getattr(context,attr)
	xd = parse_math_string(x)
	yd = parse_math_string(y)
	zd = parse_math_string(z)
	assert a == Vector(xd,yd,zd)


@then('{attr1:w} = normalize({attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a == b.normalize()

@then('every pixel of {attr} is color({r:g},{g:g},{b:g})')
def step_impl(context,attr,r,g,b):
	for i in getattr(context,attr).pixels:
		for j in i:
			assert j.color == Color(r,g,b)

@then('pixel_at({canvas},{x:d},{y:d}) = {color}')
def step_impl(context,canvas, x, y, color):
	canvas = getattr(context,canvas)
	clr = getattr(context,color)
	assert canvas.pixels[y][x].color == clr


@then('lines {range_begin:d}-{range_end:d} of {attr} are')
def step_impl(context,range_begin, range_end, attr):
	rng = range(range_begin- 1,range_end - 1) # Ranges will not match array indices initially
	ppm = getattr(context,attr)
	ppm_lines = ppm.splitlines()
	text_lines = context.text.splitlines()
	print(f'PPM: {ppm_lines}')
	print(f'Test: {text_lines}')
	text_counter = 0
	for i in rng:
	    assert ppm_lines[i] == text_lines[text_counter]
	    text_counter += 1

@then('{attr} ends with a newline character')
def step_impl(context,attr):
	ppm = getattr(context,attr)
	assert ppm[-1] == '\n'

@then('{attr}.{dimension:w} = {x:g}')
def step_impl(context,attr,dimension,x):
	t = getattr(context,attr)
	assert getattr(t,dimension) == x

@then('{attr1:w}.{prop:w} = {attr2:w}')
def step_impl(context,attr1,prop,attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	p = getattr(a,prop)
	assert p == b

@then('{attr} = tuple({x:g},{y:g},{z:g},{w:g}')
def step_impl(context,attr,x,y,z,w):
	assert getattr(context,attr) == Tuple(x,y,z,w)

@then('{attr} != tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,x,y,z,w):
	assert getattr(context,attr) != Tuple(x,y,z,w)

@then('{attr} is a point')
def step_impl(context,attr):
	assert getattr(context,attr).w == 1.0


@then('{attr} is not a vector')
def step_impl(context,attr):
	assert getattr(context,attr).w == 1.0

@then('{attr} is not a point')
def step_impl(context,attr):
	assert getattr(context,attr).w == 0.0


@then('{attr} is a vector')
def step_impl(context,attr):
	assert getattr(context,attr).w == 0.0

@then('{attr1} + {attr2} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context, attr1, attr2,x,y,z,w):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a+b == Tuple(x,y,z,w)

@then('-{attr} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,x,y,z,w):
	t = getattr(context,attr) 
	assert -t == Tuple(x,y,z,w)

@then('{attr} * {num:g} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,num,x,y,z,w):
	t = getattr(context,attr)
	assert t * num == Tuple(x,y,z,w)

@then('{attr} / {num:g} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,num,x,y,z,w):
	t = getattr(context,attr)
	assert t / num == Tuple(x,y,z,w)

@then('{attr} = tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,x,y,z,w):
	t = getattr(context,attr) 
	assert t.x == x \
		and t.y == y \
		and t.z == z \
		and t.w == w

@then('{attr1} - {attr2} = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a-b == Vector(x,y,z)

@then('{attr1} - {attr2} = point({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a-b == Point(x,y,z)

@then('magnitude({attr}) = sqrt({num:g})')
def step_impl(context,attr,num):
	v = getattr(context,attr)
	assert math.isclose(v.magnitude,math.sqrt(num),rel_tol=1e-10)

@then('magnitude({attr}) = {num:g}')
def step_impl(context,attr,num):
	v = getattr(context,attr)
	assert v.magnitude == num

@then('normalize({attr}) = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	v = getattr(context,attr)
	assert v.normalize() == Vector(x,y,z)

@then('dot({attr1},{attr2}) = {num:g}')
def step_impl(context,attr1,attr2,num):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	assert a.dot(b) == num

@then('cross({attr1},{attr2}) = vector({x:g},{y:g},{z:g})')
def step_impl(context,attr1,attr2,x,y,z):
	a = getattr(context,attr1)
	b= getattr(context,attr2)
	assert a.cross(b) == Vector(x,y,z)

@then('repr({attr}) == \'Tuple({x:g},{y:g},{z:g},{w:g})\'')
def step_impl(context,attr,x,y,z,w):
	t = getattr(context,attr)
	assert repr(t) == f'Tuple({x},{y},{z},{w})'

@then('{attr}.{color} = {val:g}')
def step_impl(context,attr,color,val):
	c = getattr(context,attr)
	assert getattr(c,color) == val

@then('{attr1} + {attr2} = color({r:g},{g:g},{b:g})')
def step_impl(context,attr1,attr2,r,g,b):
	c1 = getattr(context,attr1)
	c2 = getattr(context,attr2)
	assert c1 + c2 == Color(r,g,b)

@then('{attr1} - {attr2} = color({r:g},{g:g},{b:g})')
def step_impl(context,attr1,attr2,r,g,b):
	c1 = getattr(context,attr1)
	c2 = getattr(context,attr2)
	assert c1 - c2 == Color(r,g,b)

@then('{attr} * {scalar:g} = color({r:g},{g:g},{b:g})')
def step_impl(context,attr,scalar,r,g,b):
	c = getattr(context,attr)
	assert c * scalar == Color(r,g,b)

@then('{attr1} * {attr2:w} = color({r:g},{g:g},{b:g})')
def step_impl(context,attr1,attr2,r,g,b):
	c1 = getattr(context,attr1)
	c2 = getattr(context,attr2)
	assert c1 * c2 == Color(r,g,b)

@then('{attr:w} is nothing')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a is None 

@then('{attr:w} is nothing')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a is None 
