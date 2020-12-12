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


function solution(data) {
  let acc = 0;
  let pos = 0;
  const executed = new Set();

  while (true) {
    const currentInst = data[pos];

    if (executed.has(pos)) {
      break;
    }

    executed.add(pos);

    const [newAcc, nextPos] = calculate(currentInst.split(" "), acc, pos);
    acc = newAcc;
    pos = nextPos;
  }

  // console.log(executed);
  console.log(acc);
}

solution(data);
