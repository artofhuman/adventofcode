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

puts cptch.call('1122').inspect
puts cptch.call('1111').inspect
puts cptch.call('1234').inspect
puts cptch.call('91212129').inspect
