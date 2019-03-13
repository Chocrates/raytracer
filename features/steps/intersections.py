from Intersection import *

@when('{attr1:w} intersection({x:g},{attr2:w})')
@given('{attr1:w} intersection({x:g},{attr2:w})')
def step_impl(context,attr1,x,attr2):
	s = getattr(context,attr2)
	setattr(context,attr1,Intersection(x,s))

@when('{attr1:w} intersections({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,Intersections(a,b))


