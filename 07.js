const { count } = require("console");

function readFile() {

    let fs = require("fs");
    //let arr = fs.readFileSync("prueba.txt").toString().split("\n");
    let arr = fs.readFileSync("input07.txt").toString().split("\n");


    array=arr[0].split(',');//.map(Number);
    return array;

}

function get_median(values) {

    values.sort( function(a,b) {return a - b;} );

    var half = Math.floor(values.length/2);

    if(values.length % 2==0)
        return values[half];
    else
        return (values[half-1] + values[half]) / 2.0;
}

function get_average(values){

    let total=0;

    for(let pos of positions){

        total+=parseInt(pos)

    }

    return parseInt(total/values.length)

}


function main_p1(){

    let median=get_median(positions)

    let fuel=0;

    for (let pos of positions){

        fuel+=Math.abs(parseInt(pos)-median)

    }

    return fuel;
}

function get_fuel(steps){

    let counter=0;

    for(let i=1;i<steps;i++){

        counter+=i

    }

    return counter;
}


function main_p2(){

    let avg=get_average(positions)
    console.log(avg)

    let fuel=0;

    for (let pos of positions){

        fuel+=Math.abs(parseInt(pos)-avg)+get_fuel(Math.abs(parseInt(pos)-avg))

    }

    return fuel;
}

var positions=readFile()

console.log(`Part 1: ${main_p1()}\n`)
console.log(`Part 2: ${main_p2()}\n`)



/* La gracia es :

    -> Part 1 : hay que encontrar un valor más cercano para todos = usamos mediana


    -> Part 2 : como cuesta mas cada paso que das , hay que buscar el valor medio para que se muevan lo menos posible

*/
