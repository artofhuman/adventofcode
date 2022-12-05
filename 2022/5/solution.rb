stacks = []
commands = []

content = File.readlines("input.txt", chomp: true)

content.each do |line|
  if line.include?("[")
    items = []
    (1..line.size).step(4) do |i|
      value = line[i]
      stack_i = i / 4
      stack = stacks[stack_i]
      if stack.nil?
        stack = []
        stacks << stack
      end

      stack << value if value != " "
    end
  elsif line.include?("move")
    commands << line.scan(/\d+/).map(&:to_i)
  end
end

def result(stacks, commands, part:)
  res = stacks.map(&:dup)
  commands.each do |command|
    count, from, to = command
    elems = res[from - 1].shift(count)

    elems.reverse! if part == 1
    res[to - 1].insert(0, *elems)
  end

  res.inject("") do |acc, stack|
    acc << stack.first
  end
end

puts result(stacks, commands, part: 1)
puts result(stacks, commands, part: 2)
