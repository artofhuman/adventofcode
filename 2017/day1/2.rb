# part 2
def solution(input)
  sum = 0
  length = input.size

  digits = input.chars.map(&:to_i)

  digits.each.with_index do |digit, i|
    next_digit = digits[(i + (length / 2)) % length]

    sum += digit if digit == next_digit
  end

  sum
end
