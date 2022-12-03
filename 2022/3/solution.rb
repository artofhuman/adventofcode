require 'set'

content = File.readlines("input.txt", chomp: true)

costs = ('a'..'z').zip(1..26).to_h
costs2 = ('A'..'Z').zip(27..52).to_h

costs.merge!(costs2)

part1 = content.inject(0) do |acc, line|
  mid = line.size / 2
  p1 = line[...mid]
  p2 = line[mid...]
  char = p1.chars.to_set.intersection(p2.chars.to_set).to_a[0]

  acc += costs.fetch(char)
end

part2 = 0
content.each_slice(3) do |group|
  value = group.map { _1.chars.to_set }.reduce(&:intersection).to_a[0]
  part2 += costs.fetch(value)
end

puts part1
puts part2
