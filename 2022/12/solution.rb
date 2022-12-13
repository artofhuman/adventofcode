input = File.readlines("input.txt", chomp: true)

GRID = []

input.each  { |line| GRID << line.chars }

M = GRID.size
N = GRID.first.size

HEIGHTS = ('a'..'z').zip(1..26).to_h
VISITED = []

start, stop = nil
M.times do |i|
  VISITED << [false] * N

  N.times do |j|
    char = GRID[i][j]
    start = [i, j] if char == "S"
    stop = [i, j] if char == "E"
  end
end

def height(char)
  case char
  when "S"
    0
  when "E"
    HEIGHTS["z"]
  else
    HEIGHTS[char]
  end
end

def value(pos)
  l, r = pos

  return nil if l < 0
  return nil if r < 0

  GRID.dig(l, r)
rescue
  puts "debug"
  puts pos.inspect
  raise
end

def neighbors(cur)
  l, r = cur
  left = [l, r - 1]
  top = [l - 1, r]
  right = [l, r + 1]
  bottom = [l + 1, r]

  cur_value = value(cur)
  cur_height = height(cur_value)

  [left, top, right, bottom].select do |new_pos|
    new_value = value(new_pos)
    next false if new_value.nil?
    next_height = height(new_value)

    next_height <= cur_height + 1
  end
end


def part1(start, stop)
  q = [start]
  distances = {start => 0}

  until q.empty?
    cur = q.shift
    distance = distances[cur]

    neighbors(cur).each do |neighbor|
      if distances[neighbor].nil?# || distances[neighbor] > distance + 1
        q << neighbor
        distances[neighbor] = distance + 1
      end
    end
  end

  distances[stop]
end

puts "part1"
puts part1(start, stop)

def part2(stop)
  distances = []
  M.times do |i|
    N.times do |j|
      if GRID[i][j] == "a"
        distances << part1([i, j], stop)
      end
    end
  end

  distances.compact!.min
end

puts "part2"
puts part2(stop)
