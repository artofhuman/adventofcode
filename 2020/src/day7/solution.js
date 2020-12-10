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
                graph[parent].push(child);
            });
        }
    });

    return graph;
}

function findBags(bags, bag, acc) {
    for (const parent in bags) {
        const childs = bags[parent];

        if (childs.includes(bag)) {
            acc.add(parent);
            findBags(bags, parent, acc);
        }
    }

    return acc;
}

function solution(data) {
    const graph = parse(data);

    const sum = findBags(graph, myBag, new Set()).size;

    console.log(sum);
}

solution(data);
