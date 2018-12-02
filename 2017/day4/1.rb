def valid?(line)
  words = line.split(' ')
  words.uniq.size == words.size
end

def solution(input)
  input.split("\n").each.inject(0) do |acc, line|
    valid?(line) ? acc + 1 : acc
  end
end

root = File.expand_path(File.dirname(__FILE__))

input = File.read("#{root}/input.txt")
puts solution(input)
