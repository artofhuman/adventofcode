# part 1
class Captcha
  def call(input)
    digits = input.chars.map(&:to_i)

    similar_digits = []

    digits.each.with_index do |digit, i|
      next_digit = digits[i + 1] || digits.first

      if digit == next_digit
        similar_digits << digit
      end
    end

    similar_digits.sum
  end
end

cptch = Captcha.new

puts cptch.call('1122')
puts cptch.call('1111')
puts cptch.call('1234')
puts cptch.call('91212129')

# part 2
def solution(input)
  sum = 0
  length = input.size

  digits = input.chars.map(&:to_i)

  digits.each.with_index do |digit, i|
    next_digit = digits[(i + (length / 2)) % length]

    sum += digit if (digit == next_digit)
  end

  sum
end
