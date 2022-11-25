// program to generate fibonacci series up to a certain number

// take input from the user
const number = 10;
let n1 = 0, n2 = 1, nextTerm;
nextTerm = n1 + n2;

while (nextTerm <= number) {
    n1 = n2;
    n2 = nextTerm;
    nextTerm = n1 + n2;
}
console.log(nextTerm);