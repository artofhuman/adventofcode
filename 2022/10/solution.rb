require "set"
input = File.readlines("input.txt", chomp: true)

INTERESTED = Set[20, 60, 100, 140, 180, 220]

State = Struct.new(:cycle, :x) do
  def value
    cycle * x
  end

  def to_s
    "cycle=#{cycle} x=#{x} value=#{value}"
  end
end

def run(input)
  cycle = 1
  x = 1

  Enumerator.new do |yielder|
    input.each do |line|
      case line.split(" ")
      in ["noop"]
        yielder << State.new(cycle, x)
        cycle += 1
      in ["addx", value]
        2.times do |i|
          yielder << State.new(cycle, x)
          cycle += 1
        end

        x += value.to_i
        yielder << State.new(cycle, x)
      end
    end
  end
end

def part1(input)
  result = Set.new
  run(input).each do |state|
    result.add(state) if INTERESTED.include? state.cycle
  end
  result.map(&:value).sum
end

puts part1(input)
