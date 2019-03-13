from Sphere import *
from Translation import *
import importlib

@given('{attr:w} sphere()')
def step_impl(context,attr):
    setattr(context,attr,Sphere())

@when('{attr1:w} intersects({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
    a = getattr(context,attr2)
    b = getattr(context,attr3)
    setattr(context,attr1,b.intersects(a))


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

@when('set_transform({attr1:w},{attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	a.transform = b

@when('set_transform({attr:w},{method:w}({x:g},{y:g},{z:g}))')
def step_impl(context,attr,method,x,y,z):
	a = getattr(context,attr)
	# Extra hacky, capitalize the first char for the class name
	transform = getattr(importlib.import_module('Translation'),method.capitalize())
	a.transform = transform(x,y,z)
