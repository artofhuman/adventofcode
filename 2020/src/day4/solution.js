import { readFileSync } from 'fs';


const CID = "cid";
const REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
];

function readFile(filePath) {
    return readFileSync(filePath, 'utf8').trim().split('\n\n');
}

const testInput = readFile("src/day4/input.txt");

function solution(input) {
    let result = 0;
    input.forEach(passport => {
        if (REQUIRED_FIELDS.every(field => {
            return passport.includes(field);
        })) {
            result++;
        }
        // console.log(passport);
    });

    console.log("result", result);
}

solution(testInput);
