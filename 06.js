const { count } = require("console");

function readFile() {

    let fs = require("fs");
    let arr = fs.readFileSync("input06.txt").toString().split("\n");


    array=arr[0].split(',');//.map(Number);

}


function main_p1(){

    for(let i=1;i<=DAYS_P1;i++){

        for(let j=0;j<array.length;j++){

            if(array[j]==0){

                array[j]=RESET_DAYS;
                array_aux.push(NEW_DAYS);
            }

            else{

                array[j]-=1;
            }

        }

         for(let k=0;k<array_aux.length;k++){
            

            array.push(array_aux[k]);

            
        }

        array_aux=[];

    }

    return array.length;


}

function main_p2(){

    array=[];
    readFile();

    var days_array=[];
    days_array.length=9;

    for(let i=0;i<days_array.length;i++){

        days_array[i]=0;
    }

    for(let i=0;i<array.length;i++){

        days_array[array[i]]+=1;

    }

    for(let i=1;i<=DAYS_P2;i++){

        //* mover 1 a la izquierda 
        //* una vez en 0 -> sumar a 8 el mismo numero que haya y añadir la misma cantidad a 6

        aux=parseInt(days_array[0]);
        days_array[0]= days_array[1];
        days_array[1]= days_array[2];
        days_array[2]= days_array[3];
        days_array[3]= days_array[4];
        days_array[4]= days_array[5];

        days_array[5]= days_array[6];
        days_array[6]= days_array[7]+aux;
        days_array[7]= days_array[8];
        days_array[8]=aux;
    }

    //* SUMAR TODAS ETAPAS


    let count=0;

    for(let i=0;i<days_array.length;i++){

        count+=days_array[i];
    }
    
    return count;

}

var DAYS_P1=80;
var DAYS_P2=256;
var RESET_DAYS=6;
var NEW_DAYS=8;

var array=[];
readFile();
var array_aux=[];

console.log(`Part 1: ${main_p1()} \n`);
console.log(`Part 2: ${main_p2()} \n`);
