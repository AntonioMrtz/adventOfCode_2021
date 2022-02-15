//Clean input into array
var fs = require("fs");
const school = fs
  .readFileSync("input06.txt", "utf8")
  .split(",")
  .map(x => parseInt(x))  
//Initialize 9 element long array with zero's
let initialState = new Array(); for (let i=0; i<9; ++i) initialState[i] = 0;
//Sort array of local lanternfish school into groups based on lifecycle status
school.map( (element) => {
    initialState[element]++
})
//Number of days to count
//const days = 256;
const days = 120;

//Loop to iterate through array, aging lanternfish and creating new ones as required
for(let i = 0; i<days; i++) {
    let dayZero = initialState[0]
    let dayOne = initialState[1]
    let dayTwo = initialState[2]
    let dayThree = initialState[3]
    let dayFour = initialState[4]
    let dayFive = initialState[5]
    let daySix = initialState[6]
    let daySeven = initialState[7]
    let dayEight = initialState[8]
    initialState[0] = dayOne
    initialState[1] = dayTwo
    initialState[2] = dayThree
    initialState[3] = dayFour
    initialState[4] = dayFive
    initialState[5] = daySix
    initialState[6] = daySeven + dayZero
    initialState[7] = dayEight
    initialState[8] = dayZero
}

//Final Log Statement
console.log(initialState.reduce((a,b)=>a+b))