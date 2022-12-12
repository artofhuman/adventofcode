TestDiv = Struct.new(:div, :if_true, :if_false)
Monkey = Struct.new(:items, :operation, :test, :counter) do
  def incr
    self.counter += 1
  end
end

# monkey0 = Monkey.new([79, 98], "old * 19", TestDiv.new(23, 2, 3), 0)
# monkey1 = Monkey.new([54, 65, 75, 74], "old + 6", TestDiv.new(19, 2, 0), 0)
# monkey2 = Monkey.new([79, 60, 97], "old * old", TestDiv.new(13, 1, 3), 0)
# monkey3 = Monkey.new([74], "old + 3", TestDiv.new(17, 0, 1), 0)

# monkeys = [monkey0, monkey1, monkey2, monkey3]

def monkeys
  monkey0 = Monkey.new([57, 58], "old * 19", TestDiv.new(7, 2, 3), 0)
  monkey1 = Monkey.new([66, 52, 59, 79, 94, 73], "old + 1", TestDiv.new(19, 4, 6), 0)
  monkey2 = Monkey.new([80], "old + 6", TestDiv.new(5, 7, 5), 0)
  monkey3 = Monkey.new([82, 81, 68, 66, 71, 83, 75, 97], "old + 5", TestDiv.new(11, 5, 2), 0)
  monkey4 = Monkey.new([55, 52, 67, 70, 69, 94, 90], "old * old", TestDiv.new(17, 0, 3), 0)
  monkey5 = Monkey.new([69, 85, 89, 91], "old + 7", TestDiv.new(13, 1, 7), 0)
  monkey6 = Monkey.new([75, 53, 73, 52, 75], "old * 7", TestDiv.new(2, 0, 4), 0)
  monkey7 = Monkey.new([94, 60, 79], "old + 2", TestDiv.new(3, 1, 6), 0)
  return [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
end

def calculate(item, operation)
  case operation.split(" ")
  in ["old", operation, "old"]
    return item * item if operation == "*"
    return item + item if operation == "+"
    return item - item if operation == "-"
  in ["old", operation, points]
    return item * points.to_i if operation == "*"
    return item + points.to_i if operation == "+"
    return item - points.to_i if operation == "-"
  end
end

def play_round(monkeys)
  monkeys.each do |monkey|
    while item = monkey.items.shift do
      monkey.incr

      new_item = calculate(item, monkey.operation)
      new_item = (new_item / 3).ceil
      if new_item % monkey.test.div == 0
        monkeys[monkey.test.if_true].items << new_item
      else
        monkeys[monkey.test.if_false].items << new_item
      end
    end
  end
end


def play_round2(monkeys)
  big_mod = monkeys.map { |m| m.test.div }.reduce(&:*)

  monkeys.each do |monkey|
    while item = monkey.items.shift do
      monkey.incr

      new_item = calculate(item, monkey.operation)
      new_item %= big_mod

      if new_item % monkey.test.div == 0
        monkeys[monkey.test.if_true].items << new_item
      else
        monkeys[monkey.test.if_false].items << new_item
      end
    end
  end
end

def part1(monkeys)
  20.times do |i|
    play_round(monkeys)
  end

  m1, m2 = monkeys.sort_by! { |m| m.counter }.last(2)
  puts m1.counter * m2.counter
end

def part2(monkeys)
  10000.times do |i|
    play_round2(monkeys)
  end

  m1, m2 = monkeys.sort_by! { |m| m.counter }.last(2)
  puts m1.counter * m2.counter
end

part1(monkeys)
part2(monkeys)

