'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}

class SinglyLinkedListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    insertNode(data) {
        const node = new SinglyLinkedListNode(data);
        if (!this.head) this.head = node;
        else this.tail.next = node;
        this.tail = node;
    }
}

function printLinkedList(head) {
    let temp = head;
    while (temp) {
        console.log(temp.data);
        temp = temp.next;
    }
}

function main() {
    const llistCount = parseInt(readLine(), 10);
    const llist = new SinglyLinkedList();
    for (let i = 0; i < llistCount; i++) {
        llist.insertNode(parseInt(readLine(), 10));
    }
    printLinkedList(llist.head);
}
