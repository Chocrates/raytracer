from behave import *
import importlib
import copy
import re
import math

from Matrix import *
from Tuple import *
from Translation import *
from Ray import *
from Sphere import *
from Canvas import *
from Material import *
from Light import *

def parse_math_string(num_string):
	""" Parses square root, pi, and e in a number into a python representation """
	num_string = re.sub(r'√(\d+)', r'math.sqrt(\1)',num_string.lower())
	num_string = re.sub(r'π', r'math.pi',num_string.lower())
	num_string = re.sub(r'e', r'math.e',num_string.lower())
	ns = {}
	exec(f'import math; out = {num_string}', {} , ns)
	return ns['out']

def parse_rotation_axis(axis):
	if axis == 'x':
		return Rotation.Axis.X
	elif axis == 'y':
		return Rotation.Axis.Y
	elif axis == 'z':
		return Rotation.Axis.Z

# Yuck, I can either do a parse or regex step matcher, not both :/
@given('the following matrix {attr:w}')
def step_impl(context,attr):
	setattr(context,attr,Matrix.build_matrix(context.text))

@given('the following {x:g}x{y:g} matrix {attr:w}')
def step_impl(context,x,y,attr):
	setattr(context,attr,Matrix.build_matrix(context.text))

@given('{attr:w} transpose(identity_matrix)')
def step_impl(context,attr):
	setattr(context,attr,Matrix.identity().transpose())

@given('{attr1} submatrix({attr2},{row:d},{col:d})')
def step_impl(context,attr1,attr2,row,col):
	a = getattr(context,attr2)
	setattr(context,attr1,a.submatrix(row,col))

@given('{attr1:w} inverse({attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr2)
	setattr(context,attr1,a.inverse())

@given('{attr1:w} = {attr2:w} * {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,a*b)

@given('{attr:w} translation({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Translation(x,y,z))

@given('{attr:w} scaling({xs:S},{ys:S},{zs:S}) * rotation_{axiss:w}({rads:S})')
def step_impl(context,attr,xs,ys,zs,axiss,rads):
	x = parse_math_string(xs)
	y = parse_math_string(ys)
	z = parse_math_string(zs)
	axis = parse_rotation_axis(axiss)
	print(f'Rads: {rads}')
	rad = parse_math_string(rads)
	setattr(context,attr,Scaling(x,y,z) * Rotation(axis,rad))
	print(f'Transformation matirx: {(Scaling(x,y,z) * Rotation(axis,rad)).data}')


@given('{attr:w} scaling({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Scaling(x,y,z))

@given('{attr:w} rotation_{axis:w}({rad:S})')
def step_impl(context,attr,axis,rad):
	rot_axis = parse_rotation_axis(axis)
	setattr(context,attr,Rotation(rot_axis,parse_math_string(rad)))

@given('{attr:w} shearing({x_y:g},{x_z:g},{y_x:g},{y_z:g},{z_x:g},{z_y:g})')
def step_impl(context,attr,x_y,x_z,y_x,y_z,z_x,z_y):
	print(f'Shearing: {Shearing(x_y,x_z,y_x,y_z,z_x,z_y).data}')
	setattr(context,attr,Shearing(x_y,x_z,y_x,y_z,z_x,z_y))

@given('{attr:w} ray(point({px:g},{py:g},{pz:g}),vector({vx:g},{vy:g},{vz:g}))')
def step_impl(context,attr,px,py,pz,vx,vy,vz):
	setattr(context,attr,Ray(Point(px,py,pz),Vector(vx,vy,vz)))

@given('{attr:w} sphere()')
def step_impl(context,attr):
	setattr(context,attr,Sphere())

@given('{attr} canvas({width:d},{height:d})')
def step_impl(context,attr,width,height):
	setattr(context,attr,Canvas(width,height))

@given('{attr} tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,x,y,z,w):
	setattr(context, attr, Tuple(x,y,z,w))

@given('{attr} point({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Point(x,y,z))

@given('{attr:w} vector({xs:S},{ys:S},{zs:S})')
def step_impl(context,attr,xs,ys,zs):
	x = parse_math_string(xs)
	y = parse_math_string(ys)
	z = parse_math_string(zs)
	setattr(context,attr,Vector(x,y,z))

@given('{attr} color({r:g},{g:g},{b:g})')
def step_impl(context,attr,r,g,b):
	setattr(context,attr,Color(r,g,b))

@when('{attr1:w} intersection({x:g},{attr2:w})')
@given('{attr1:w} intersection({x:g},{attr2:w})')
def step_impl(context,attr1,x,attr2):
	s = getattr(context,attr2)
	setattr(context,attr1,Intersection(x,s))

@when('{attr1:w} intersections({attr2:w},{attr3:w})')
@given('{attr1:w} intersections({attr2:w},{attr3:w})')
@given('{attr1:w} intersections({attr2:w},{attr3:w},{attr4:w},{attr5:w})')
def step_impl(context,attr1,**kwargs):
	attributes = []
	for key,attr in kwargs.items():
		attributes.append(getattr(context,attr))
	setattr(context,attr1,Intersections(*attributes))


@given('{attr1:w}.{prop:w} {num:g}')
def step_impl(context,attr1,prop,num):
	a = getattr(context,attr1)
	b = getattr(a,prop)
	b = num

@given('{attr:w} material()')
def step_impl(context,attr):
	setattr(context,attr, Material())

@given('{attr:w} point_light(point({px:g},{py:g},{pz:g}),color({cx:g},{cy:g},{cz:g}))')
def step_impl(context,attr,px,py,pz,cx,cy,cz):
	setattr(context,attr,PointLight(Point(px,py,pz),Color(cx,cy,cz)))
