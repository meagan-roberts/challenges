/**
 * FizzBuzz Challenge - Write a program that counts from 1 to 100 with a twist:

    - for numbers that are multiples of 3, you should print "Fizz" instead.
    - for multiples of 5, print "Buzz".
    - for numbers that are multiples of both 3 and 5, print "FizzBuzz".
    
    - create a loop that goes through numbers 1 to 100
    - use the modulo operator (%) to check if a number is a multiple of 3, 5, or both
    - depending on the result, print "Fizz", "Buzz", or "FizzBuzz"
    - if a number isn't a multiple of 3 or 5, just print the number itself
 */

function fizzBuzz() {

    console.log("FizzBuzz Challenge!")

    // set count start
    let count = 1;

    // while count is less than 100 check each number and console log it
    while (count <= 100) {
        if (count % 3 === 0 && count % 5 === 0) {
            console.log("FizzBuzz")
            count++
        } else if (count % 3 === 0) {
            console.log("Fizz")
            count++
        } else if (count % 5 === 0) {
            console.log("Buzz")
            count++
        } else {
            console.log(count)
            count++
        }
        
    }
}