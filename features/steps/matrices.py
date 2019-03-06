from behave import *
from Matrix import *
import math

# Yuck, I can either do a parse or regex step matcher, not both :/
@given('the following matrix {attr:w}')
def step_impl(context,attr):
	setattr(context,attr,Matrix.build_matrix(context.text))

@given('the following {x:g}x{y:g} matrix {attr:w}')
def step_impl(context,x,y,attr):
	setattr(context,attr,Matrix.build_matrix(context.text))

@then('{attr:w}[{x:d},{y:d}] = {num:g}')
def step_impl(context,attr,x,y,num):
	m = getattr(context,attr)
	assert math.isclose(m.data[x][y],num,rel_tol=1e-10)

@then('{attr:w}[{x:d},{y:d}] = {numerator:d}/{denominator:d}')
def step_impl(context,attr,x,y,numerator,denominator):
	m = getattr(context,attr)
	assert math.isclose(m.data[x][y],numerator/denominator,rel_tol=1e-10)

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


@given('{attr:w} transpose(identity_matrix)')
def step_impl(context,attr):
	setattr(context,attr,Matrix.identity().transpose())

@then('determinant({attr:w}) = {num:g}')
def step_impl(context,attr,num):
	a = getattr(context,attr)
	assert a.determinant() == num

@then('submatrix({attr:w},{row:d},{col:d}) is the following {x:g}x{y:g} matrix')
def step_impl(context,attr,row,col,x,y):
	a = getattr(context,attr)
	assert a.submatrix(row,col) == Matrix.build_matrix(context.text)

@given('{attr1} submatrix({attr2},{row:d},{col:d})')
def step_impl(context,attr1,attr2,row,col):
	a = getattr(context,attr2)
	setattr(context,attr1,a.submatrix(row,col))

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

@given('{attr1:w} inverse({attr2:w})')
def step_impl(context,attr1,attr2):
	a = getattr(context,attr2)
	setattr(context,attr1,a.inverse())

@then('{attr:w} is the following {x:d}x{y:d} matrix')
def step_impl(context,attr,x,y):
	a = getattr(context,attr)
	assert a == Matrix.build_matrix(context.text)

@then('inverse({attr:w}) is the following {x:d}x{y:d} matrix')
def step_impl(context,attr,x,y):
	a = getattr(context,attr)
	assert a.inverse() == Matrix.build_matrix(context.text)

@given('{attr1:w} = {attr2:w} * {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr2)
	b = getattr(context,attr3)
	setattr(context,attr1,a*b)

@then('{attr1:w} * inverse({attr2:w}) = {attr3:w}')
def step_impl(context,attr1,attr2,attr3):
	a = getattr(context,attr1)
	b = getattr(context,attr2)
	c = getattr(context,attr3)
	assert a * b.inverse() == c


