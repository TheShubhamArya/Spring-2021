// Shubham Arya
// 1001650536
// 02/24/2021

//inputtable array is created and intialized with values.
var inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 10];
//printing out the contents of the inputtable array
console.log("inputtable array: ", inputtable);

//Function five takes in a number and returns a multiple of 5
function five(number){
  return number * 5;
}
//Each value of inputtable is passed into five by using map which is then multiplied by 5 and put into fiveTable
let fiveTable = inputtable.map(five);
//Prints out the contents of fiveTable
console.log("Contents of fiveTable are: ",fiveTable);

//Function thirteen takes in a number and returns a multiple of 13
function thirteen(number){
  return number * 13;
}
//Each value of inputtable is passed into thirteen by using map which is then multiplied by 13 and put into thriteenTable
let thirteenTable = inputtable.map(thirteen);
//Prints out the contents of thirteenTable
console.log("Contents of thirteenTable are: ",thirteenTable)

//Function square takes in a number and returns a square of the same number by multiplying itself.
function square(number){
  return number*number;
}
//Each value of inputtable is passed into square by using map which is then multiplied by itself to give square of it
let squaresTable = inputtable.map(square);
//Prints out the contents of squaresTable
console.log("Contents of squaresTable are: ",squaresTable);

//This variable stores the multiples of 5 which will later be used to display the output
var multipleOf5 = [];
//Takes a start and end variable. Eg 1 and 100 in this case
function oddMultiplesOFFive(start, end) {
  //Execute as long as start is less than or equal to end
  if (start <= end) {
    // checks if start is divisble by 5 and checks if start is not divisble by 2
    if ((start % 5 == 0) && (start % 2 == 1)) {
      //If the value is an odd multiple of 5, then push the value into the multipleOf5 array
      multipleOf5.push(start)
    }
    //recursively calls itself by incrementing the start index by 1
    return oddMultiplesOFFive(start + 1, end)
  }
  // if the index has exceeded the end number, then it returns the multipleOf5 variable
  return multipleOf5
}
//Prints out the contents of multipleOf5 which has odd mutliple of 5 from 1 to 100
console.log("Output for odd multiples of 5: ",oddMultiplesOFFive(1, 100));


//Declare an empty array that will store even multiple of 7
var multipleOf7 = [];
//declare and intialize a variable that sums up the even multiple of 7
var sum = 0
//This takes in a start, end value. In this case, the start and end will be 1, 100 respectively
function sumSeven(start, end) {
  //Execute as long as start is less than or equal to end
  if (start <= end) {
    //checks if start is divisble by 7 as well as divisble by 2
    if ((start % 7 == 0) && (start % 2 == 0)) {
      //If the value is an even multiple of 7, then push the value into the multipleOf7 array
      multipleOf7.push(start)
      //adds the even multiple of 7 to the sum
      sum += start
    }
    //If the number if not an even multiple of 7, then increment the start by 1 but keep the sum as it is.
    return sumSeven(start + 1, end)
  }
  // returns the array that has the even multiples of 7 in it
  return multipleOf7
}
//Prints out the contents for even multipleOf7 which has even multiple of 7 from 1 and 100
console.log("Output for evem multiples of 7: ",sumSeven(1,100));
//Prints out the sum of even multiple of 7
console.log("sum is ", sum);

//Using currying for this function
//to run this, the function call should be cylinder_volume(5)(10) when r = 5 and h = 10
function cylinder_volume(r) {
  //returns a function with parameter h
  return function(h) {
    //function inside function where the volume of the cylinder is calculated
    return 3.14 * r * r * h;
  }
}
//Prints out the value returned by the function cylinder_volume
console.log("Volume of cylinder: " + cylinder_volume(5)(10));

//function provided in the question
makeTag = function(beginTag, endTag) {
  return function(textcontent) {
    return beginTag + textcontent + endTag;
  };
};
//tag_table currying for table
tag_table = makeTag("<table>\n", "</table>");
//tag_tr currying for tr
tag_tr = makeTag("<tr>\n", "</tr>\n");
//tag_th currying for th
tag_th = makeTag("<th>", "</th>\n");
//tag_td currying for td
tag_td = makeTag("<td>", "</td>\n");

//for the heading, <th> tags are added
table_header = tag_th("Player") + tag_th("Speciality") + tag_th("Salary");
//entire header row gets <tr> tags
entire_table = tag_tr(table_header);

//for second row, <td> tags are added
table_detail1 = tag_td("Kohli") + tag_td("Batting") + tag_td("5,000,000");
//table_detail1 row gets <tr> tags
entire_table += tag_tr(table_detail1);

//for third row, <td> tags are added
table_detail2 = tag_td("Pant") + tag_td("Keeping") + tag_td("3,000,000");
//table_detail2 row gets <tr> tags
entire_table += tag_tr(table_detail2);

//for fourth row, <td> tags are added
table_detail3 = tag_td("Bumrah") + tag_td("Bowler") + tag_td("4,500,000");
//table_detail3 row gets <tr> tags
entire_table += tag_tr(table_detail3);

//tables tags added to entire_table
final_table = tag_table(entire_table);
//printing out the table
console.log(final_table);


console.log("Extra credit: ");
// number array stores the number
var numberArray = [];
// this is a generic function that tames 4 parameters
// start- number to start with
// end- when the program should halt
// multiple- to find the multiple of a number
// evenOrOdd- whether the multiple has to be even or odd
function genericFunc(start, end, multiple, evenOrOdd) {
  //if the start is less than or equal to ebd
  if (start <= end) {
    //if evenOrOdd is 1, then the it checks if number is odd, otherwise it checks if number is even
    if (evenOrOdd == 1) {
      // checks if the current number is a multiple of the passed multiple number in the function
      if ((start % multiple == 0) && (start % 2 == 1)) {
        //if it is an odd multiple of "multiple", then pushes into numberArray
        numberArray.push(start)
      }
    } else {
      // checks if the current number is a multiple of the passed multiple number in the function
      if ((start % multiple == 0) && (start % 2 == 0)) {
          //if it is an even multiple of "multiple", then pushes into numberArray
        numberArray.push(start)
      }
    }
    // start value is incremented each time and the function is recursively called
    return genericFunc(start + 1, end, multiple, evenOrOdd)
  }
  // returns the numberArray that has the values stored
  return numberArray
}
//Prints out the generic function values
//Here, i am checking for even multiple of 7 that start from 1 and end at 100
console.log("Output for even multiples of 7: ",genericFunc(1, 100,7,2));
//Here, i am checking for odd multiple of 5 that start from 1 and end at 100
numberArray = []; //clearing out the contents of the numberArray from the previous call
console.log("Output for odd multiples of 5: ",genericFunc(1, 100,5,1));
