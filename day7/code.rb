require 'set'
require 'pry-byebug'

root = File.expand_path(File.dirname(__FILE__))
input = File.read("#{root}/input.txt")

#input = <<~EOF
#pbga (66)
#xhth (57)
#ebii (61)
#havc (66)
#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
#qoyq (66)
#padx (45) -> pbga, havc, qoyq
#tknk (41) -> ugml, padx, fwft
#jptl (61)
#ugml (68) -> gyxo, ebii, jptl
#gyxo (61)
#cntj (57)
#EOF

REGEXP = /(?<name>[a-z]+) \((?<weight>[0-9]+)\)(?: -> (?<childs>[a-z, ]+))?/
tree = []

class Node
  attr_accessor :name, :weight, :childs

  def initialize(name, weight, childs)
    @name = name
    @weight = weight
    @childs = Array(childs)
  end
end

input.split("\n").each do |line|
  name, weight, childs = REGEXP.match(line).captures

  tree << {name => {weight: weight, childs: Array(childs&.split(', '))}}
end

tos = tree.flat_map do |item|
  item.values.first[:childs]
end

root = (Set.new(tree.flat_map(&:keys)) - Set.new(tos)).to_a.first


TREE = tree

def node_weigth(item, acc = 0)
  childs = item.values.first[:childs]
  weight = item.values.first[:weight].to_i

  acc += weight
  return acc if childs.empty?

  childs.each do |child_name|
    node = TREE.find { |i| i.keys.first == child_name }
    acc = node_weigth(node, acc)
  end

  acc
end

def find_node(name)
  TREE.find { |i| i.keys.first == name }
end

weights = {}

tree.each do |node|
  name = node.keys.first
  childs = node.values.first[:childs]

  next if name == root
  next if childs.empty?

  weights[name] = node_weigth(node)
end

unbalanced = find_node('ndjsvna')
unbalanced = find_node('orflty')
unbalanced = find_node('ncrxh')
