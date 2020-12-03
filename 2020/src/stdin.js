import { readFileSync } from 'fs';

export function toNums(elems) {
    return elems.map(function (elem) {
        return parseInt(elem);
    })
}

export function readFile(filePath) {
    return readFileSync(filePath, 'utf8').trim().split("\n");
}

export function readNums(filePath) {
    const input = readFile(filePath);
    return toNums(input);
}

