const { start } = require("repl");

function readFile() {
    let fs = require("fs");
    //let array_aux = fs.readFileSync("input05.txt").toString().split("\n");
    let array_aux = fs.readFileSync("prueba.txt").toString().split("\n");


    for (i in array_aux) {
        array.push(array_aux[i]);
    }

}

function getEntries(line){

    line=line.trim();
    line=line.split(" -> ");

    let start=line[0];
    let end=line[1];

    start=start.split(",");
    end=end.split(",");


    let start_x=start[0];
    let start_y=start[1];
    let end_x=end[0];
    let end_y=end[1];

    fillEntries(parseInt(start_x),parseInt(start_y),parseInt(end_x),parseInt(end_y));


}

function fillEntries(start_x,start_y,end_x,end_y){

    // si nos encontramos un 1 ponemos 2
    // si encontramos 2 dejamos igual

    console.log(start_x,start_y,end_x,end_y);

    if(start_x==end_x){

        if(start_y>end_y){

            for(let i=end_y;i<start_y;i++){

                if(entries.get())
                entries.set(start_x,i);

            }


        }

        else {

            for(let i=start_y;i<end_y;i++){

                entries.set(start_x,i);

            }


        }

    }

    else if(start_y==end_y){

        if(start_x>end_x){

            for(let i=end_x;i<start_x;i++){

                console.log(entries[i]);
                entries[i]+=1;


                if(entries[i]==null){

                    console.log("ifwjuiwjwf");
                }

            }


        }

        else {


            for(let i=start_x;i<end_x;i++){

                console.log(entries[i]);
                entries[i]+=1;


            }


        }

    }


    //console.log(`start ${start} end ${end}\n`);

}

function checkResult(){

    // del entries comprobar los numeros 2 que hay

    let counter=0;

    //TODO

    return counter;

}

var array=[];
var entries=new Map();


var result=0;


readFile();

for (let line of array){

    getEntries(line);
    //console.log(entries);

}

//console.log(`Part 1: ${checkResult()} \n`);


