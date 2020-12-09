import { readFileSync } from 'fs';

export function toNums(elems) {
    return elems.map(function (elem) {
        return parseInt(elem);
    })
}

export function readFile(filePath, split="\n") {
    const data = readFileSync(filePath, 'utf8').trim();
    if (split.length) {
        return data.split(split);
    }
    return data;
}

export function readNums(filePath) {
    const input = readFile(filePath);
    return toNums(input);
}

