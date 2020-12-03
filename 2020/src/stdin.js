import { readFileSync } from 'fs';

export function toNums(elems) {
    return elems.map(function (elem) {
        return Number(elem);
    })
}

export function readNums(filePath) {
    const input = readFileSync(filePath, 'utf8').split("\n");
    return toNums(input);
}