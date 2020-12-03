import { readFileSync } from 'fs';

export function toNums(elems) {
    return elems.map(function (elem) {
        return parseInt(elem);
    })
}

export function readNums(filePath) {
    const input = readFileSync(filePath, 'utf8').trim().split("\n");
    return toNums(input);
}