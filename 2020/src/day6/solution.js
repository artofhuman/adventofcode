import { readFile } from "../stdin.js";

const groupsData = readFile("src/day6/input.txt", "\n\n");

function calculate(groups) {
    let result = 0;
    groups.forEach(group => {
        const answers = new Set(group.split("\n").join(''));
        result += answers.size
    });

    return result;
}

console.log(calculate(groupsData));
