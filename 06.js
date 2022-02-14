
function readFile() {
    let fs = require("fs");
    let arr = fs.readFileSync("input06.txt").toString().split("\n");
    //let arr = fs.readFileSync("prueba.txt").toString().split("\n");


    array=arr[0].split(',');//.map(Number);
    //var arrayOfNumbers = arrayOfStrings.map(Number);
    /*for (i in array_aux) {
        array.push(array_aux[i]);
    }*/


}


function main_p1(){

    for(let i=1;i<=DAYS;i++){

        for(let j=0;j<array.length;j++){

            if(array[j]==0){

                array[j]=6;
                array_aux.push(8);
            }

            else{

                array[j]-=1;
                //console.log(array[j]);
            }

        }

        //console.log(array_aux);
         for(let k=0;k<array_aux.length;k++){
            

            array.push(array_aux[k]);

            
        }
        // 
        
        //array.push(array_aux);
        array_aux=[];

    }

    return array.length;


}

var DAYS=160;
var RESET_DAYS=6;
var NEW_DAYS=8;

var array=[];
readFile();
var array_aux=[];

console.log(`Part 1: ${main_p1()} \n`);
