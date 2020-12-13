import { readFile } from "../stdin.js";

const numbers = readFile("src/day9/input.txt").map(e => parseInt(e, 10));

console.log(numbers);

const preambleSize = 25;

function hasSumOfTwo(numbers, target) {
    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < numbers.length; j++) {
            const a = numbers[i];
            const b = numbers[j];
            if (a != b) {
                if ( a + b === target) {
                    return true;
                }
            }
        }
    }

    return false;
}

function part1(numbers) {
    for (let i = preambleSize; i < numbers.length; i++) {
        const num = numbers[i];

        const window = numbers.slice(i - preambleSize, i);
        const isValid = hasSumOfTwo(window, num);
        if (!isValid) {
            console.log(num);
        }
    }
}

part1(numbers);
