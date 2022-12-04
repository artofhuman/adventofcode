content = File.readlines("input.txt", chomp: true)

class Pair
  attr_reader :_begin, :_end

  def initialize(value)
    @_begin, @_end = value.split("-").map(&:to_i)
  end

  def cover?(other)
    _begin <= other._begin && _end >= other._end
  end

  def overlap?(other)
    _end >= other._begin &&  _begin <= other._end
  end
end

def build(line)
  line.split(",").map { |e| Pair.new(e) }
end

part1 = content.sum do |line|
  first, last = build(line)
  first.cover?(last) || last.cover?(first) ? 1 : 0
end

part2 = content.sum do |line|
  first, last = build(line)
  first.overlap?(last) ?  1 : 0
end

puts part1
puts part2
