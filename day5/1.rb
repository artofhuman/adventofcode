def draw(input, position)
  result = input.dup
  result[position] = "(#{result[position]})"

  puts result.join(' ').inspect
end

def solution(input)
  position = 0
  acc = 0

  while input[position]
    #draw(input, position)

    value = input[position]
    input[position] += 1
    position = position + value
    acc += 1
  end

  acc
end

#puts solution([0, 3, 0, 1, -3]).inspect

root = File.expand_path(File.dirname(__FILE__))
input = File.read("#{root}/input.txt").split("\n").map(&:to_i)
puts solution(input).inspect
