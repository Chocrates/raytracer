module Raytracer
  class Tuple
    attr_reader :x, :y, :z, :w

    def initialize(x, y, z, w)
      @x = x.to_f
      @y = y.to_f
      @z = z.to_f
      @w = w.to_f
    end

    def is_point?
      w == 1.0
    end

    def is_vector?
      w == 0.0
    end

    def ==(other)
      other.x - @x < Raytracer::EPSILON &&
        other.y - @y < Raytracer::EPSILON &&
        other.z - @z < Raytracer::EPSILON &&
        other.w - @w < Raytracer::EPSILON
    end

    def +(other)
      Tuple.new(@x + other.x, @y + other.y, @z + other.z, @w + other.w)
    end

    def -(other)
      Tuple.new(@x - other.x, @y - other.y, @z - other.z, @w - other.w)
    end

    def *(other)
      puts "Other is #{other.class}"
      puts "Other #{other}"
      if other.instance_of?(Tuple)
        Tuple.new(@x * other.x, @y * other.y, @z * other.z, @w * other.w)
      elsif other.is_a? Numeric
        Tuple.new(@x * other, @y * other, @z * other, @w * other)
      else
        raise TypeError, "Can't multiply #{self.class} with #{other.class}"
      end
    end

    def !
      Tuple.new(-@x, -@y, -@z, -@w)
    end

    def /(other)
      if other.is_a? Numeric
        Tuple.new(@x / other, @y / other, @z / other, @w / other)
      else
        raise TypeError, "Can't divide #{self.class} by #{other.class}"
      end
    end

    def dot(other)
      @x * other.x + @y * other.y + @z * other.z + @w * other.w
    end

    def cross(other)
      Tuple.new(@y * other.z - @z * other.y,
                @z * other.x - @x * other.z,
                @x * other.y - @y * other.x,
                0.0)
    end

    def magnitude
      if @w == 0.0
        Math.sqrt(@x * @x + @y * @y + @z * @z)
      else
        raise TypeError, "Can't take magnitude of a point"
      end
    end

    def normalize
      if @w == 0.0
        Tuple.new @x / magnitude, @y / magnitude, @z / magnitude, @w / magnitude
      else
        raise TypeError, "Can't take magnitude of a point"
      end
    end

    def to_s
      "(#{@x}, #{@y}, #{@z}, #{@w})"
    end
  end

  class Point < Tuple
    def initialize(x, y, z)
      super(x, y, z, 1.0)
    end
  end

  class Vector < Tuple
    def initialize(x, y, z)
      super(x, y, z, 0.0)
    end
  end
end
