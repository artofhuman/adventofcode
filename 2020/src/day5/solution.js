import { readFile } from "../stdin.js";

// const testRow = "BBFFBBFRLL";

const rows = readFile('src/day5/input.txt');

function getSitId(row) {
    const chars = row.split('')
    const rows = chars.slice(0, 7);
    let loBound = 0;
    let hiBound = 128;
    rows.forEach(char => {
        let mid = (loBound + hiBound) / 2;
        if (char == "F") {
            hiBound = mid;
        } else {
            loBound = mid;
        }
    });

    const sits = chars.slice(-3);
    let loSitBound = 0;
    let hiSitBound = 8;
    sits.forEach(sit => {
        let midSit = (loSitBound + hiSitBound) / 2;
        if (sit == "L") {
            hiSitBound = midSit;
        } else {
            loSitBound = midSit;
        }
    });

    const sitId = (loBound * 8) + loSitBound;
    return sitId;
}

const allIds = rows.map(getSitId);
const maxId = Math.max(...allIds);
const minId = Math.min(...allIds);

let i = minId;
while (i <= maxId) {
    if (!(allIds.includes(i))) {
        console.log(i);
    }
    i++;
}
