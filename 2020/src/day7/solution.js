import { readFile  } from "../stdin.js";

const data = readFile("src/day7/input.txt");

const noChildsRe = /^((\w+ \w+))/;
const childRe = /^(\d+) ((\w+ \w+))/;
const parentRe = /^((\w+ \w+)) bags contain (.*)\./;
const myBag = "shiny gold";

function parse(data) {
    const graph = {};

    data.forEach(row => {
        if (row.includes("no other bags")) {
            const [, parent] = noChildsRe.exec(row);
            graph[parent] = [];
        } else {
            const [, parent, _, other] = parentRe.exec(row);

            graph[parent] = [];

            other.split(', ').forEach(contains => {
                const [_, _childCount, child] = childRe.exec(contains);
                const data = {"color": child, "count": parseInt(_childCount, 10)};
                graph[parent].push(data);
            });
        }
    });

    return graph;
}

function findBags(bags, bag, acc) {
    for (const parent in bags) {
        const childs = bags[parent];

        const colors = [];
        for (let i = 0; i < childs.length; i++) {
            const color = childs[i]["color"];
            colors.push(color);
        }

        if (colors.includes(bag)) {
            acc.add(parent);
            findBags(bags, parent, acc);
        }
    }

    return acc;
}

function calculateBags(bags, bag) {
    const childs = bags[bag];
    let total = 0;

    if (childs) {
        for (let i = 0; i < childs.length; i++) {
            const color = childs[i]["color"];
            const count = childs[i]["count"];
            total += count + (count * calculateBags(bags, color));
        }
    }

    return total;
}

function part1(data) {
    const graph = parse(data);

    const sum = findBags(graph, myBag, new Set()).size;
    console.log(sum);
}

function part2(data) {
    const graph = parse(data);

    const sum = calculateBags(graph, myBag);

    console.log(sum);
}

part1(data);
part2(data);
