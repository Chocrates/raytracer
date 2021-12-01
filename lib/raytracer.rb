# frozen_string_literal: true

require 'require_all'

module Raytracer
  EPSILON = 0.00001
  class Error < StandardError; end
end

require_rel 'raytracer'
