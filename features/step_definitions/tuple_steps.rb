require_relative '../../lib/raytracer'

Given('a ← tuple\({float}, {float}, {float}, {float})') do |_float, _float2, _float3, _float4|
  @a = Raytracer::Tuple.new(_float, _float2, _float3, _float4)
end

Then('a.x = {float}') do |_float|
  expect(@a.x).to eq(_float)
end

Then('a.y = {float}') do |_float|
  expect(@a.y).to eq(_float)
end

Then('a.z = {float}') do |_float|
  expect(@a.z).to eq(_float)
end

Then('a.w = {float}') do |_float|
  expect(@a.w).to eq(_float)
end

Then('a is a point') do
  expect(@a.is_point?).to be true
end

Then('a is not a vector') do
  expect(@a.is_vector?).to be false
end

Then('a is not a point') do
  expect(@a.is_point?).to be false
end

Then('a is a vector') do
  expect(@a.is_vector?).to be true
end

Given('p ← point\({int}, {int}, {int})') do |_int, _int2, _int3|
  @p = Raytracer::Point.new(_int, _int2, _int3)
end

Then('p = tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  @p = Raytracer::Tuple.new(_int, _int2, _int3, _int4)
end

Given('v ← vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  @v = Raytracer::Vector.new(_int, _int2, _int3)
end

Then('v = tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  expect(@v == Raytracer::Tuple.new(_int, _int2, _int3, _int4)).to be true
end

Given('a1 ← tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  @a1 = Raytracer::Tuple.new(_int, _int2, _int3, _int4)
end

Given('a2 ← tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  @a2 = Raytracer::Tuple.new(_int, _int2, _int3, _int4)
end

Then('a1 + a2 = tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  puts 'Got a plus!'
  expect(@a1 + @a2).to eq(Raytracer::Tuple.new(_int, _int2, _int3, _int4))
end

Then('a1 - a2 = tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  puts 'Got a minus!'
  expect(@a1 - @a2).to eq(Raytracer::Tuple.new(_int, _int2, _int3, _int4))
end

Given('p1 ← point\({int}, {int}, {int})') do |_int, _int2, _int3|
  @p1 = Raytracer::Point.new(_int, _int2, _int3)
end

Given('p2 ← point\({int}, {int}, {int})') do |_int, _int2, _int3|
  @p2 = Raytracer::Point.new(_int, _int2, _int3)
end

Then('p1 + p2 = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@p1 + @p2).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Then('p1 - p2 = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@p1 - @p2).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Then('p - v = point\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@p - @v).to eq(Raytracer::Point.new(_int, _int2, _int3))
end

Given('v1 ← vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  @v1 = Raytracer::Vector.new(_int, _int2, _int3)
end

Given('v2 ← vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  @v2 = Raytracer::Vector.new(_int, _int2, _int3)
end

Then('v1 - v2 = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@v1 - @v2).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Given('zero ← vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  @zero = Raytracer::Vector.new(_int, _int2, _int3)
end

Then('zero - v = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@zero - @v).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Then('-a = tuple\({int}, {int}, {int}, {int})') do |_int, _int2, _int3, _int4|
  expect(!@a).to eq(Raytracer::Tuple.new(_int, _int2, _int3, _int4))
end

Then('a * {float} = tuple\({float}, {float}, {float}, {float})') do |_float, _float2, _float3, _float4, _float5|
  expect(@a * _float).to eq(Raytracer::Tuple.new(_float2, _float3, _float4, _float5))
end

Then('a \/ {float} = tuple\({float}, {float}, {float}, {float})') do |_float, _float2, _float3, _float4, _float5|
  expect(@a / _float).to eq(Raytracer::Tuple.new(_float2, _float3, _float4, _float5))
end

Then('magnitude\(v) = {float}') do |_float|
  expect(@v.magnitude).to eq(_float)
end

Then('magnitude\(v) = √{float}') do |_float|
  expect(@v.magnitude).to eq(Math.sqrt(_float))
end

Then('normalize\(v) = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@v.normalize).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Then('normalize\(v) = approximately vector\({float}, {float}, {float})') do |_float, _float2, _float3|
  expect(@v.normalize).to eq(Raytracer::Vector.new(_float, _float2, _float3))
end

Then('dot\(v, w) = {float}') do |_float|
  expect(@v.dot(@w)).to eq(_float)
end

When('norm ← normalize\(v)') do
  @norm = @v.normalize
end

Then('magnitude\(norm) = {int}') do |_int|
  expect(@norm.magnitude).to eq(_int)
end

Given('a ← vector\({float}, {float}, {float})') do |_float, _float2, _float3|
  @a = Raytracer::Vector.new(_float, _float2, _float3)
end

Given('b ← vector\({float}, {float}, {float})') do |_float, _float2, _float3|
  @b = Raytracer::Vector.new(_float, _float2, _float3)
end

Then('dot\(a, b) = {int}') do |_int|
  expect(@a.dot(@b)).to eq(_int)
end

Then('cross\(a, b) = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@a.cross(@b)).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Then('cross\(b, a) = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  expect(@b.cross(@a)).to eq(Raytracer::Vector.new(_int, _int2, _int3))
end

Given('c ← color\({float}, {float}, {float})') do |_float, _float2, _float3|
  @c = Raytracer::Color.new(_float, _float2, _float3)
end

Then('c.red = {float}') do |_float|
  expect(@c.red).to eq(_float)
end

Then('c.green = {float}') do |_float|
  expect(@c.green).to eq(_float)
end

Then('c.blue = {float}') do |_float|
  expect(@c.blue).to eq(_float)
end

Given('c1 ← color\({float}, {float}, {float})') do |_float, _float2, _float3|
  @c1 = Raytracer::Color.new(_float, _float2, _float3)
end

Given('c2 ← color\({float}, {float}, {float})') do |_float, _float2, _float3|
  @c2 = Raytracer::Color.new(_float, _float2, _float3)
end

Then('c1 + c2 = color\({float}, {float}, {float})') do |_float, _float2, _float3|
  expect(@c1 + @c2).to eq(Raytracer::Color.new(_float, _float2, _float3))
end

Then('c1 - c2 = color\({float}, {float}, {float})') do |_float, _float2, _float3|
  expect(@c1 - @c2).to eq(Raytracer::Color.new(_float, _float2, _float3))
end

Then('c * {float} = color\({float}, {float}, {float})') do |_float, _float2, _float3, _float4|
  expect(@c * _float).to eq(Raytracer::Color.new(_float2, _float3, _float4))
end

Then('c1 * c2 = color\({float}, {float}, {float})') do |_float, _float2, _float3|
  expect(@c1 * @c2).to eq(Raytracer::Color.new(_float, _float2, _float3))
end

Given('n ← vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  # Given('n ← vector\({int}, {int}, {float})') do |int, int2, float|
  # Given('n ← vector\({int}, {float}, {int})') do |int, float, int2|
  # Given('n ← vector\({int}, {float}, {float})') do |int, float, float2|
  # Given('n ← vector\({float}, {int}, {int})') do |float, int, int2|
  # Given('n ← vector\({float}, {int}, {float})') do |float, int, float2|
  # Given('n ← vector\({float}, {float}, {int})') do |float, float2, int|
  # Given('n ← vector\({float}, {float}, {float})') do |float, float2, float3|
  pending # Write code here that turns the phrase above into concrete actions
end

When('r ← reflect\(v, n)') do
  pending # Write code here that turns the phrase above into concrete actions
end

Then('r = vector\({int}, {int}, {int})') do |_int, _int2, _int3|
  # Then('r = vector\({int}, {int}, {float})') do |int, int2, float|
  # Then('r = vector\({int}, {float}, {int})') do |int, float, int2|
  # Then('r = vector\({int}, {float}, {float})') do |int, float, float2|
  # Then('r = vector\({float}, {int}, {int})') do |float, int, int2|
  # Then('r = vector\({float}, {int}, {float})') do |float, int, float2|
  # Then('r = vector\({float}, {float}, {int})') do |float, float2, int|
  # Then('r = vector\({float}, {float}, {float})') do |float, float2, float3|
  pending # Write code here that turns the phrase above into concrete actions
end

Given('n ← vector\(√{int}\/{int}, √{int}\/{int}, {int})') do |_int, _int2, _int3, _int4, _int5|
  # Given('n ← vector\(√{int}\/{int}, √{int}\/{int}, {float})') do |int, int2, int3, int4, float|
  # Given('n ← vector\(√{int}\/{int}, √{int}\/{float}, {int})') do |int, int2, int3, float, int4|
  # Given('n ← vector\(√{int}\/{int}, √{int}\/{float}, {float})') do |int, int2, int3, float, float2|
  # Given('n ← vector\(√{int}\/{int}, √{float}\/{int}, {int})') do |int, int2, float, int3, int4|
  # Given('n ← vector\(√{int}\/{int}, √{float}\/{int}, {float})') do |int, int2, float, int3, float2|
  # Given('n ← vector\(√{int}\/{int}, √{float}\/{float}, {int})') do |int, int2, float, float2, int3|
  # Given('n ← vector\(√{int}\/{int}, √{float}\/{float}, {float})') do |int, int2, float, float2, float3|
  # Given('n ← vector\(√{int}\/{float}, √{int}\/{int}, {int})') do |int, float, int2, int3, int4|
  # Given('n ← vector\(√{int}\/{float}, √{int}\/{int}, {float})') do |int, float, int2, int3, float2|
  # Given('n ← vector\(√{int}\/{float}, √{int}\/{float}, {int})') do |int, float, int2, float2, int3|
  # Given('n ← vector\(√{int}\/{float}, √{int}\/{float}, {float})') do |int, float, int2, float2, float3|
  # Given('n ← vector\(√{int}\/{float}, √{float}\/{int}, {int})') do |int, float, float2, int2, int3|
  # Given('n ← vector\(√{int}\/{float}, √{float}\/{int}, {float})') do |int, float, float2, int2, float3|
  # Given('n ← vector\(√{int}\/{float}, √{float}\/{float}, {int})') do |int, float, float2, float3, int2|
  # Given('n ← vector\(√{int}\/{float}, √{float}\/{float}, {float})') do |int, float, float2, float3, float4|
  # Given('n ← vector\(√{float}\/{int}, √{int}\/{int}, {int})') do |float, int, int2, int3, int4|
  # Given('n ← vector\(√{float}\/{int}, √{int}\/{int}, {float})') do |float, int, int2, int3, float2|
  # Given('n ← vector\(√{float}\/{int}, √{int}\/{float}, {int})') do |float, int, int2, float2, int3|
  # Given('n ← vector\(√{float}\/{int}, √{int}\/{float}, {float})') do |float, int, int2, float2, float3|
  # Given('n ← vector\(√{float}\/{int}, √{float}\/{int}, {int})') do |float, int, float2, int2, int3|
  # Given('n ← vector\(√{float}\/{int}, √{float}\/{int}, {float})') do |float, int, float2, int2, float3|
  # Given('n ← vector\(√{float}\/{int}, √{float}\/{float}, {int})') do |float, int, float2, float3, int2|
  # Given('n ← vector\(√{float}\/{int}, √{float}\/{float}, {float})') do |float, int, float2, float3, float4|
  # Given('n ← vector\(√{float}\/{float}, √{int}\/{int}, {int})') do |float, float2, int, int2, int3|
  # Given('n ← vector\(√{float}\/{float}, √{int}\/{int}, {float})') do |float, float2, int, int2, float3|
  # Given('n ← vector\(√{float}\/{float}, √{int}\/{float}, {int})') do |float, float2, int, float3, int2|
  # Given('n ← vector\(√{float}\/{float}, √{int}\/{float}, {float})') do |float, float2, int, float3, float4|
  # Given('n ← vector\(√{float}\/{float}, √{float}\/{int}, {int})') do |float, float2, float3, int, int2|
  # Given('n ← vector\(√{float}\/{float}, √{float}\/{int}, {float})') do |float, float2, float3, int, float4|
  # Given('n ← vector\(√{float}\/{float}, √{float}\/{float}, {int})') do |float, float2, float3, float4, int|
  # Given('n ← vector\(√{float}\/{float}, √{float}\/{float}, {float})') do |float, float2, float3, float4, float5|
  pending # Write code here that turns the phrase above into concrete actions
end
