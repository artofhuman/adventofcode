import { readFile } from "../stdin.js";

const data = readFile("src/day8/input.txt");

function parseInst(instruction) {
  const [name, value] = instruction;
  return [name, parseInt(value, 10)]
}

function calculate(instruction, acc, pos) {
  const [name, value] = parseInst(instruction);

  switch (name) {
    case "nop":
      return [acc, pos + 1];
    case "acc":
      return [acc + value, pos + 1];
    case "jmp":
      return [acc, pos + value];
  }
}

function part1(data) {
  let acc = 0;
  let pos = 0;
  const executed = new Set();

  while (data.length != pos) {
    const currentInst = data[pos];

    if (executed.has(pos)) {
      return [acc, true]
    }

    executed.add(pos);

    const [newAcc, nextPos] = calculate(currentInst.split(" "), acc, pos);
    acc = newAcc;
    pos = nextPos;
  }

  return [acc, false]
}

function getPositions(data, name) {
  const pos = [];
  for (let i = 0; i < data.length; i++) {
    const line = data[i];
    if (line.includes(name)) {
      pos.push(i);
    }
  }

  return pos;
}

function part2(data) {
  const jmpPositions = getPositions(data, 'jmp');

  // just check jmp first and its right guess
  jmpPositions.forEach(posiblePos => {
    const newLine = data[posiblePos].replace("jmp", "nop");
    const newData = [...data];
    newData[posiblePos] = newLine;

    const [acc, isLoop] = part1(newData);

    console.log(isLoop, acc);
  });
}

console.log(part1(data));
console.log(part2(data));
