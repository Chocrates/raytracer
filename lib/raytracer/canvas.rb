module Raytracer
  class Canvas
    attr_accessor :width, :height, :pixels

    def initialize(width, height, color = Color.new(0, 0, 0))
      @width = width
      @height = height
      @pixels = Array.new(height) { Array.new(width) { color } }
    end

    def write_pixel(x, y, color)
      @pixels[y][x] = color
    end

    def pixel_at(x, y)
      @pixels[y][x]
    end

    def to_ppm
      "P3\n#{width} #{height}\n255\n" +
        @pixels.map do |row|
          r = row.map do |pixel|
            "#{pixel} "
          end.join.strip
          r[r[0..70].rindex(/ /)] = "\n" if r.length > 70
          r
        end.join("\n").strip + "\n"
    end
  end
end
