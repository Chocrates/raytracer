from Sphere import *

@given('{attr:w} sphere()')
def step_impl(context,attr):
    setattr(context,attr,Sphere())

@when('{attr1:w} intersects({attr2:w},{attr3:w})')
def step_impl(context,attr1,attr2,attr3):
    a = getattr(context,attr2)
    b = getattr(context,attr3)
    setattr(context,attr1,b.intersects(a))


@then('{attr:w}[{idx:d}] = {val:g}')
def step_impl(context,attr,idx,val):
    a = getattr(context,attr)
    assert a[idx] == val
