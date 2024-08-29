// import { apiKey } from "./util";
// import apiKey from "./util.js";
// import { apiKey, abc as content } from "./util";  // 한꺼번에 여러개 import 가능
import * as util from "./util.js"  // util.js에서 전부 가져옴

// // console.log(apiKey);
console.log(util.apiKey);

// Variables
// Variables stores values >> resuability, readabuility
const userMessage = "Hello World!"

// userMessage = "New value"; // const; 재할당 불가 

console.log(userMessage); // String
console.log(userMessage);


// Operators
console.log( 10 + 5 );
console.log('hello' + 'world');
console.log(10 === 5); // return boolean

if (10 === 10) {
    console.log("works");
}

// Functions & Parameters
function greet() {
    console.log('Hello!');
}

greet();
greet();
greet();
greet();
greet();

function creatGreeting(userName, message = "Hello!") {
    // console.log(userName);
    // console.log(message);

    return "Hi, I am " + userName + "." + message;
}

console.log(creatGreeting('Max')); 

const greeting = creatGreeting('Manuel', "Hello, what's up?");
console.log(greeting);
