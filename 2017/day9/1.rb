require 'pry-byebug'

def assert(expected, item)
  raise "#{expected} != #{item}" if expected != item
end

def solution(input)
  level = 1
  sum = 0
  garbage = false
  cancel = false
  garbage_count = 0

  input.chars do |ch|
    if cancel
      cancel = false
    elsif garbage && ch == '!'
      cancel = true
    elsif garbage && ch != '>'
      garbage_count += 1
    elsif ch == '<'
      garbage = true
    elsif ch == '>'
      garbage = false
    elsif ch == '{'
      level += 1
    elsif ch == '}'
      level -= 1
      sum += level unless cancel
    end
  end

  [sum, garbage_count]
end


#assert(1, solution('{}'))
#assert(6, solution('{{{}}}'))
#assert(5, solution('{{},{}}'))
#assert(16, solution('{{{},{},{{}}}}'))

#assert 1, solution('{<a>,<a>,<a>,<a>}')
#assert 9, solution('{{<ab>},{<ab>},{<ab>},{<ab>}}')
#assert 9, solution('{{<!!>},{<!!>},{<!!>},{<!!>}}')
#assert 3, solution('{{<a!>},{<a!>},{<a!>},{<ab>}}')
#assert 29, solution('{},{{{}}},{<a>,<a>,<a>,<a>},{{<ab>},{<ab>},{<ab>},{<ab>}},{{<!!>},{<!!>},{<!!>},{<!!>}},{{<a!>},{<a!>},{<a!>},{<ab>}}')

root = File.expand_path(File.dirname(__FILE__))
input = File.read("#{root}/input.txt")

puts solution(input).inspect
