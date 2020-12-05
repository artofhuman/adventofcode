import { readFileSync } from 'fs';

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
const colorRegex = /^#([0-9a-f]{6})$/;
const eclValues = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
const pidRegex = /^\d{9}$/;


function isValidRange(min, max, value) {
    return value >= min && value <= max
}


function isValid(data, fieldName) {
    let value = data.get(fieldName);

    switch (fieldName) {
        case "byr":
            value = parseInt(value, 10);
            return isValidRange(1920, 2002, value);
        case "iyr":
            value = parseInt(value, 10);
            return isValidRange(2010, 2020, value);
        case "eyr":
            value = parseInt(value, 10);
            return isValidRange(2020, 2030, value);
        case "hgt":
            const num = parseInt(value, 10);
            if (value.endsWith("cm")) {
                return isValidRange(150, 193, num);
            } else if (value.endsWith("in")) {
                return isValidRange(59, 76, num);
            }
        case "hcl":
            return colorRegex.test(value);
        case "ecl":
            return eclValues.includes(value);
        case "pid":
            return pidRegex.test(value);
        default:
            return false;
    }
}

function solution(input) {
    let result = 0;
    input.forEach(passport => {
        passport = passport.replace(/\n/g, " ");
        const data = new Map(passport.split(" ").map(s => s.split(":")));
        let invalid = [];
        if (REQUIRED_FIELDS.every(field => {
            const valid = passport.includes(field) && isValid(data, field);
            if (!valid) {
                invalid.push(field);
            }
            return valid;
        })) {
            result++;
        } else {
            console.log("==", passport, invalid);
        }
    });

    console.log("result", result);
}

solution(testInput);
