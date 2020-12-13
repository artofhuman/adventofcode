import { readFile } from "../stdin.js";

const numbers = readFile("src/day9/input.txt").map(e => parseInt(e, 10));

console.log(numbers);

const preambleSize = 25;

function hasSumOfTwo(numbers, target) {
    const checkSet = new Set(numbers);

    for (let i = 0; i < numbers.length; i++) {
        const a = numbers[i];
        const diff = target - a;

        if (checkSet.has(diff)) {
            return true;
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
