import { readFile } from "../stdin.js"

let testInput = readFile("src/day3/test_input.txt");
let input = readFile("src/day3/input.txt");

function solution(input, right, down) {
    let curPos = 0;
    let countTrees = 0;
    const width = input[0].length;

    for (let rowNum = 0; rowNum < input.length; rowNum = rowNum + down) {
        if (input[rowNum][curPos] === "#") {
            countTrees++;
        }
        curPos = (curPos + right) % width;
    }

    return countTrees;
}

const SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];

let total = 1;
SLOPES.forEach(function(slope) {
    const res = solution(input, ...slope);
    total *= res;
});

console.log(total);
