root = File.expand_path(File.dirname(__FILE__))
input = File.read("#{root}/input.txt")

REGEXP = /(?<reg>[a-z]+) (?<operation>inc|dec) (?<by>.*) if (?<cond_reg>[a-z]+) (?<eql>.*) (?<cond_eql>.*)/

registers = Hash.new
highest_value = 0

input.split("\n").each do |line|
  data = REGEXP.match(line).named_captures

  registers[data['reg']] ||= 0
  registers[data['cond_reg']] ||= 0

  if registers[data['cond_reg']].public_send(data['eql'].to_sym, data['cond_eql'].to_i)

    registers[data['reg']] = if data['operation'] == 'inc'
                              registers[data['reg']] += data['by'].to_i
                             else
                              registers[data['reg']] -= data['by'].to_i
                             end

    highest_value = registers[data['reg']] if registers[data['reg']] > highest_value
    highest_value = registers[data['cond_reg']] if registers[data['cond_reg']] > highest_value
  end

end

puts registers.inspect
puts highest_value
#puts registers.max_by { |k, v| v}[0]
