def solution(input)
  position = 0
  acc = 0

  while input[position]
    value = input[position]
    value >= 3 ? input[position] -= 1 : input[position] += 1

    position = position + value
    acc += 1
  end

  acc
end

root = File.expand_path(File.dirname(__FILE__))
input = File.read("#{root}/input.txt").split("\n").map(&:to_i)
puts solution(input).inspect
