require_relative '../../lib/raytracer'
Given('c ← canvas\({int}, {int})') do |_int, _int2|
  @c = Raytracer::Canvas.new _int, _int2
end

Then('c.width = {int}') do |_int|
  # Then('c.width = {float}') do |float|
  expect(@c.width).to eq _int
end

Then('c.height = {int}') do |_int|
  expect(@c.height).to eq _int
end

Then('every pixel of c is color\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@c.pixels.all? { |row| row.all? { |pixel| pixel == Raytracer::Color.new(_int, _int2, _int3) } }).to be true
end

Given('red ← color\({int}, {int}, {int})') do |_int, _int2, _int3|
  @red = Raytracer::Color.new _int, _int2, _int3
end

When('write_pixel\(c, {int}, {int}, red)') do |_int, _int2|
  @c.write_pixel _int, _int2, @red
end

Then('pixel_at\(c, {int}, {int}) = red') do |_int, _int2|
  expect(@c.pixel_at(_int, _int2)).to eq @red
end

When('ppm ← canvas_to_ppm\(c)') do
  @ppm = @c.to_ppm
end

Then('lines {int}-{int} of ppm are') do |_int, _int2, _doc_string|
  expect(@ppm.split("\n")[(_int - 1)..(_int2 - 1)].join("\n")).to eq _doc_string
end

Given('c3 ← color\({float}, {float}, {float})') do |_float, _float2, _float3|
  @c3 = Raytracer::Color.new _float, _float2, _float3
end

When('write_pixel\(c, {int}, {int}, c1)') do |_int, _int2|
  @c.write_pixel _int, _int2, @c1
end

When('write_pixel\(c, {int}, {int}, c2)') do |_int, _int2|
  @c.write_pixel _int, _int2, @c2
end

When('write_pixel\(c, {int}, {int}, c3)') do |_int, _int2|
  @c.write_pixel _int, _int2, @c3
end

When('every pixel of c is set to color\({float}, {float}, {float})') do |_float, _float2, _float3|
  @c.height.times do |_y|
    @c.width.times do |_x|
      color = Raytracer::Color.new _float, _float2, _float3
      @c.write_pixel _x, _y, color
    end
  end
end

Then('ppm ends with a newline character') do
  expect(@ppm.end_with?("\n")).to be true
end
