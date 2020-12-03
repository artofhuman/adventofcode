import { readFile } from "../stdin.js"

const test_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

const input = readFile("src/day2/input.txt");

const regex = /(\d*)-(\d*) (\w): (\w*)/;

function solution(input) {
    let valid_passwords = 0;
    input.forEach(function(row) {
        const [, min, max, targetChar, password] = regex.exec(row);
        let counts = 0;

        for (let i = 0; i < password.length; i++) {
            if (password[i] === targetChar) {
                counts++;
            }
        }

        if (counts >= min && counts <= max) {
            valid_passwords++;
        }
    });

    return valid_passwords;
}

console.log(solution(input));

function solution2(input) {
    let valid_passwords = 0;
    input.forEach(function(row) {
        let [, first, second, targetChar, password] = regex.exec(row);
        first = first - 1;
        second = second - 1;

        const onFirstPlace = password[first] === targetChar;
        const onSecondPlace = password[second] === targetChar;
        const valid = onFirstPlace !== onSecondPlace;
        if (valid) {
            valid_passwords++;
        }
    });

    return valid_passwords;
}

console.log(solution2(input));