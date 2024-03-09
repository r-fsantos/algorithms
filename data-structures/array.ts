// "allocates" a memory region of 6 bytes size
const a = new ArrayBuffer(6);

console.log("a:", a, "\n");

// interprets the array buffer as an 8 bit unsigned int (0 - 255 
const a8 = new Uint8Array(a);

console.log("a8:", a8);
console.log("a:", a, "\n");

a8[0] = 45;
a8[2] = 45;

console.log("a8:", a8);
console.log("a:", a, "\n");

// interprets the array buffer as an 16 bit unsigned int (0 - ?)
const a16 = new Uint16Array(a);

console.log("a16:", a16);
console.log("a:", a, "\n");

a16[2] = 90;

console.log("a16:", a16);
console.log("a:", a, "\n");

