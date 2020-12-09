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

function calculatePart2(groups) {
    let result = 0;

    groups.forEach(group => {
        const answers = group.split("\n");
        const firstPersonChars = answers[0].trim().split('');

        firstPersonChars.forEach(char => {
            let match = answers.every(a => a.includes(char));
            if (match) {
                result++;
            }
        });
    });

    return result;
}

console.log("part1", calculate(groupsData));
console.log("part2", calculatePart2(groupsData));
