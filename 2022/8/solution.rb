content = File.readlines("input.txt", chomp: true)

M = content.size
N = content.first.size

matrix = []

content.each do |line|
  matrix << line.chars.map(&:to_i)
end

border_trees = (2 * M) + (2 * N) - 4

def calculate_visible(matrix)
  total = 0
  M.times do |i|
    next if i == 0 || i == M - 1
    N.times do |j|
      next if j == 0 || j == N - 1

      left = matrix[i][0..j-1].max
      right = matrix[i][j+1..].max
      top = matrix[0..i-1].map{ _1[j] }.max
      bottom = matrix[i+1..].map{ _1[j] }.max

      h = matrix[i][j]
      is_visible = [left, right, top, bottom].any? { |s| s < h }
      total += 1 if is_visible
    end
  end
  total
end

def take(arr, h)
  new_arr = []
  arr.each do |t|
    new_arr << t
    return new_arr if t >= h
  end
  new_arr
end

def calculate_distant(matrix)
  total = 0
  M.times do |i|
    next if i == 0 || i == M - 1
    N.times do |j|
      next if j == 0 || j == N - 1

      h = matrix[i][j]

      left = take(matrix[i][0..j-1].reverse, h).size
      right = take(matrix[i][j+1..], h).size
      top = take(matrix[0..i-1].map{ _1[j] }.reverse, h).size
      bottom = take(matrix[i+1..].map{ _1[j] }, h).size

      result = left * right * top * bottom
      # puts "[#{i}, #{j} [#{left} #{right} #{top} #{bottom}]  =#{result}"
      total = result if result > total
    end
  end
  total
end

part1 = calculate_visible(matrix)
part2 = calculate_distant(matrix)

puts border_trees + part1
puts part2
