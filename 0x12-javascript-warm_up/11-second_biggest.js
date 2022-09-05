#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
} else {
    const list = process.argv;
    list.splice(null, 2);
    list.sort();
    list.pop();
    let max = Math.max(...list);
    console.log(max);
}