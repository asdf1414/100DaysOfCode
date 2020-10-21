// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

var numbers = [10, 15, 3, 7];
var k = 17;

function check(numbers, k) {
    for (var i = 0; i < numbers.length; i++) {
        firstNum = numbers[i];
        for (var x = 0; i < numbers.length; x++) {
            secondNum = numbers[x];
            result = firstNum + secondNum;
            if (result == k) { return true; }
        }
    }
}

if (check(numbers, k)) {
    alert("match found!");
}


/* more efficient approach from: aditya_kenguva#6185
* First sort the array in ascending order.
* Then take the last element subtract it from given k.
* Check to see if subtracted value is present in the array, if yes print true
* else exclude the last element and redo the loop
*/