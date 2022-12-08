content = File.readlines("input.txt", chomp: true)

Node = Struct.new(:name, :dirs, :files, :parent)

root = Node.new("/", [], [], nil)
curr_node = root
content.each do |line|
  case line.split(' ')
  in ['$', 'cd', ".."]
    curr_node = curr_node.parent
  in ['$', 'cd', name]
    next if name == "/"
    curr_node = curr_node.dirs.find { |d| d.name == name }
  in ['$', 'ls']
    next
  in ["dir", name]
    curr_node.dirs << Node.new(name, [], [], curr_node)
  in [size, String]
    curr_node.files << size.to_i
  end
end

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
UPDATE_SPACE =  30000000

def calc_size(node)
  node.files.sum + node.dirs.inject(0) { |acc, n| acc += calc_size(n) }
end

def part1(node)
  result = 0
  size = calc_size(node)
  result += size if size <= MAX_SIZE
  node.dirs.each { |dir| result += part1(dir) }
  result
end

def find_smallest(node, need_to_free)
  size = calc_size(node)
  result = TOTAL_SPACE

  result = size if size >= need_to_free

  node.dirs.each do |dir|
    sub_result = find_smallest(dir, need_to_free)
    result = sub_result if sub_result < result
  end

  result
end

def part2(root)
  root_size = calc_size(root)
  need_to_free = UPDATE_SPACE - (TOTAL_SPACE - root_size)
  find_smallest(root, need_to_free)
end

puts part2(root)
