from Canvas import *
import copy

@given('{attr} canvas({width:d},{height:d})')
def step_impl(context,attr,width,height):
	setattr(context,attr,Canvas(width,height))

@then('every pixel of {attr} is color({r:g},{g:g},{b:g})')
def step_impl(context,attr,r,g,b):
	for i in getattr(context,attr).pixels:
		for j in i:
			assert j.color == Color(r,g,b)

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

@then('pixel_at({canvas},{x:d},{y:d}) = {color}')
def step_impl(context,canvas, x, y, color):
	canvas = getattr(context,canvas)
	clr = getattr(context,color)
	assert canvas.pixels[y][x].color == clr


@when('{attr} canvas_to_ppm({canvas})')
def step_impl(context,attr,canvas):
	c = getattr(context,canvas)
	setattr(context,attr,c.generate_ppm())

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



