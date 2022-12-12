require "set"

content = File.readlines("input.txt", chomp: true)

visited = Set.new

DIRECTIONS = {
  "R" => [1, 0],
  "L" => [-1, 0],
  "U" => [0, 1],
  "D" => [0, -1]
}

class Point
  attr_reader :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def +(other)
    Point.new(x + other.x, y + other.y)
  end

  def -(other)
    Point.new(x - other.x, y - other.y)
  end

  def to_s
    "<Point x=#{x} y=#{y}>"
  end
end

head = Point.new(0, 0)
tail = Point.new(0, 0)

content.each do |line|
  dir, count_steps = line.split(" ")
  count_steps = count_steps.to_i

  puts dir, count_steps

  count_steps.times do |i|
    head += Point.new(*DIRECTIONS[dir])
    tail += head - tail

    puts "#{head} #{tail}"
    visited.add(tail)
  end
end

puts visited.inspect

# p1 = Point.new(1, 1)
# p2 = Point.new(2, 3)

# p3 = p1 + p2
# puts p3
