import { readFile } from "../stdin.js"

let testInput = readFile("src/day3/test_input.txt");
let input = readFile("src/day3/input.txt");

function move(pos, rowNum, input) {
    const row = input[rowNum]
    const char = row[pos];

    let newRow = input[rowNum].split('');
    let hasTree = false;

    if (char === "#") {
        newRow[pos] = "X";
        hasTree = true;
    } else {
        newRow[pos] = "O";
    }

    return {
        "hasTree": hasTree,
        "row": newRow.join("") // just for debug
    }
}


function solution(input) {
    let curPos = 3;
    let countTrees = 0;

    for (let i = 0; i < input.length; i++) {
        let rowNum = i + 1;

        if (rowNum < input.length) {
            const result = move(curPos, i + 1, input);
            if (curPos + 3 >= input[rowNum].length) {
                curPos = Math.abs(input[rowNum].length - (curPos + 3));
                rowNum = 0;
            } else {
                curPos = curPos + 3;
            }

            if (result['hasTree']) {
                countTrees++;
            }
        }
    }

    return countTrees;
}

const result = solution(input);
console.log("result", result);
