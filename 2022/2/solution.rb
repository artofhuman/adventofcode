lines = File.readlines("input.txt", chomp: true)

# A - Rock
# B - Paper
# C - Scissors

# X - Rock
# Y - Paper
# Z - Scissors

ELF_ROCK = "A"
ELF_PAPER = "B"
ELF_SCISSORS = "C"

YOU_ROCK = "X"
YOU_PAPER = "Y"
YOU_SCISSORS = "Z"

SHAPE_SCORES = {
  YOU_ROCK => 1,
  YOU_PAPER => 2,
  YOU_SCISSORS => 3
}

ROUND_SCORE = {
  "lose" => 0,
  "draw" => 3,
  "won" => 6
}

COMBINATIONS = {
  ELF_ROCK => {
    YOU_PAPER => "won",
    YOU_ROCK => "draw",
    YOU_SCISSORS => "lose"
  },

  ELF_PAPER => {
    YOU_PAPER => "draw",
    YOU_ROCK => "lose",
    YOU_SCISSORS => "won"
  },

  ELF_SCISSORS => {
    YOU_PAPER => "lose",
    YOU_ROCK => "won",
    YOU_SCISSORS => "draw"
  }
}

part1 = lines.inject(0) do |acc, line|
  elf, you = line.split(" ")
  result = COMBINATIONS.fetch(elf).fetch(you)
  shape_score = SHAPE_SCORES.fetch(you)
  round_score = ROUND_SCORE.fetch(result)

  acc + round_score + shape_score
end

NEEDS = {
  "X" => "lose",
  "Y" => "draw",
  "Z" => "won"
}

part2 = lines.inject(0) do |acc, line|
  elf, need = line.split(" ")
  need_result = NEEDS.fetch(need)
  hand = COMBINATIONS[elf].select do |_, res|
    res == need_result
  end.keys.first

  shape_score = SHAPE_SCORES[hand]
  round_score = ROUND_SCORE[need_result]

  acc + shape_score + round_score
end

puts part1
puts part2
