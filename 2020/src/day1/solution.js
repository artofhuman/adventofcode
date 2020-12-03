import { readNums } from "../stdin.js";

const test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
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


function solution2(nums) {
    for (let i = 0; i < nums.length; i++) {
        const a = nums[i];
        for (let j = i + 1; j < nums.length; j++) {
            const b = nums[j];
            for (let k = i + 2; k < nums.length; k++) {
                const c = nums[k];
                if (a + b + c == TARGET) {
                    return a * b * c;
                }
            }
        }
    }
 }

 function linearSolution2Enh(nums) {
    const myset = new Set();
    for (let i = 0; i < nums.length; i++) {
        myset.add(nums[i]);
    }


    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const a = nums[i];
            const b = nums[j];
            const diff = TARGET - (a + b);
            if (myset.has(diff)) {
                return diff * a * b;
            }
        }
    }
 }
// const result = solution1(input);
// console.log(result);

// console.log(linearSolution(input));

console.log(linearSolution2Enh(input));