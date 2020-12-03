import { readNums } from "../stdin.js";

const test_input = [
    "1721",
    "979",
    "366",
    "299",
    "675",
    "1456"
];

const input = readNums("src/day1/input.txt")

const TARGET = 2020;

function solution1(nums) {
   for (let i = 0; i < nums.length; i++) {
       const a = nums[i];
       for (let j = i + 1; j < nums.length; j++) {
           const b = nums[j];
           if (a + b == TARGET) {
               return a * b;
           }
       }
   }
}

function linearSolution(nums) {
    const myset = new Set();
    for (let i = 0; i < nums.length; i++) {
        const e = nums[i];
        myset.add(e);
    }

    for (let i = 0; i < nums.length; i++) {
        const e = nums[i];
        const diff = TARGET - e;
        if (myset.has(diff)) {
            return diff * e;
        }
    }
}

// const result = solution1(input);
// console.log(result);

console.log(linearSolution(input));