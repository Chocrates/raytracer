from Tuple import *
import math

@given('{attr} tuple({x:g},{y:g},{z:g},{w:g})')
def step_impl(context,attr,x,y,z,w):
	setattr(context, attr, Tuple(x,y,z,w))

@then('{attr}.{dimension:d} = {x:g}')
def step_impl(context,attr,dimension,x):
	t = getattr(context,attr)
	assert getattr(t,dimension) == x

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


@given('{attr} point({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Point(x,y,z))

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

@given('{attr} vector({x:g},{y:g},{z:g})')
def step_impl(context,attr,x,y,z):
	setattr(context,attr,Vector(x,y,z))

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

@when('{attr1} = normalize({attr2})')
def step_impl(context,attr1,attr2):
	v = getattr(context,attr2)
	setattr(context,attr1,v.normalize())

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

@given('{attr} color({r:g},{g:g},{b:g})')
def step_impl(context,attr,r,g,b):
	setattr(context,attr,Color(r,g,b))

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
