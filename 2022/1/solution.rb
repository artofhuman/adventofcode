calories = File.readlines("input.txt", chomp: true).map { |e| Integer(e) if e != "" }

group = []
calories_by_elf = calories.each_with_object([]) do |item, acc|
  if item.nil?
    acc << group
    group = []
  else
    group << item
  end
end

part1 = calories_by_elf.max_by(&:sum).sum
part2 = calories_by_elf.sort_by(&:sum).reverse.take(3).map(&:sum).sum
