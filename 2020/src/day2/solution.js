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
        const vars = regex.exec(row);
        const min = vars[1];
        const max = vars[2];
        const targetChar = vars[3];
        const password = vars[4];
        let counts = 0;

        for (let i = 0; i < password.length; i++) {
            if (password[i] === targetChar) {
                counts += 1;
            }
        }

        if (counts >= min && counts <= max) {
            valid_passwords += 1;
        }
    });

    return valid_passwords;
}

console.log(solution(input));