//Create a program in javascript that asks the user to enter 3 numbers....
const prompt = require ("prompt-sync")();
function find_largest(num1 , num2 , num3) {
if (num1 >= num2 && num1 >= num3){
console.log("largest no is:",num1)
}
else if (num2 >= num1 && num2 >= num3){
    console.log("largest no is :",num2)
}
else {
    console.log("largest no is :",num3)
}
    
}
let num1 = prompt("enter no1 :");
let num2 = prompt("enter no2 :");
let num3 = prompt("enter no3 :");

find_largest(num1,num2 , num3)