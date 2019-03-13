from Ray import *
from Tuple import *

@when('{attr1:w} ray({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,Ray(a,b))


@then('{attr:w}.count = {num:g}')
def step_impl(context,attr,num):
    a = getattr(context,attr)
    assert len(a) == num

@given('{attr:w} ray(point({px:g},{py:g},{pz:g}),vector({vx:g},{vy:g},{vz:g}))')
def step_impl(context,attr,px,py,pz,vx,vy,vz):
	setattr(context,attr,Ray(Point(px,py,pz),Vector(vx,vy,vz)))

@then('position({ray:w},{t:g}) = point({x:g},{y:g},{z:g})')
def step_impl(context,ray,t,x,y,z):
	r = getattr(context,ray)
	assert r.position(t) == Point(x,y,z)
