from Intersection import *

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

@when('{attr1:w} hit({attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr2)
	setattr(context,attr1,a.hit())

@then('{attr:w} is nothing')
def step_impl(context,attr):
	a = getattr(context,attr)
	assert a is None 
