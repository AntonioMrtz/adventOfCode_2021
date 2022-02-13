const { start } = require("repl");


//! NO ESTA MUY OPTIMIZADO , SE LE PUEDE ECHAR UN OJO

class Coordenates {

    constructor(x, y) {

        this.x = x;
        this.y = y;
        this.value = 1;


    }

    add_value() {

        this.value += 1;

    }


}

function checkIfIn(coordenate) {

    for (let i = 0; i < entries.length; i++) {

        if (entries[i].x == coordenate.x && entries[i].y == coordenate.y) {

            return entries[i];

        }


    }

    return false;

}


function addValue(coordenate) {

    for (let i = 0; i < entries.length; i++) {

        if (entries[i].x == coordenate.x && entries[i].y == coordenate.y) {

            entries[i].add_value();
        }


    }


}


function checkIfInDiagonal(coordenate) {

    for (let i = 0; i < entriesDiagonal.length; i++) {

        if (entriesDiagonal[i].x == coordenate.x && entriesDiagonal[i].y == coordenate.y) {

            return entriesDiagonal[i];

        }


    }

    return false;

}


function addValueDiagonal(coordenate) {

    for (let i = 0; i < entriesDiagonal.length; i++) {

        if (entriesDiagonal[i].x == coordenate.x && entriesDiagonal[i].y == coordenate.y) {

            entriesDiagonal[i].add_value();
        }


    }


}

///



function readFile() {
    let fs = require("fs");
    //let array_aux = fs.readFileSync("input05.txt").toString().split("\n");
    let array_aux = fs.readFileSync("input05.txt").toString().split("\n");


    for (i in array_aux) {
        array.push(array_aux[i]);
    }

}

function getEntries(line) {

    line = line.trim();
    line = line.split(" -> ");

    let start = line[0];
    let end = line[1];

    start = start.split(",");
    end = end.split(",");


    let start_x = start[0];
    let start_y = start[1];
    let end_x = end[0];
    let end_y = end[1];

    //! PONER DE NUEVO fillEntries(parseInt(start_x), parseInt(start_y), parseInt(end_x), parseInt(end_y));
    fillEntriesDiagonal(parseInt(start_x), parseInt(start_y), parseInt(end_x), parseInt(end_y));

}

function fillEntries(start_x, start_y, end_x, end_y) {

    // si nos encontramos un 1 ponemos 2
    // si encontramos 2 dejamos igual

    //console.log(start_x, start_y, end_x, end_y);

    if (start_x == end_x) {

        if (start_y > end_y) {

            for (let i = end_y; i <= start_y; i++) {


                let obj=checkIfIn(new Coordenates(start_x, i));

                if (obj!=false) {

                    addValue(obj);

                }

                else {

                    entries.push(new Coordenates(start_x,i));

                }

            }


        }

        else {

            for (let i = start_y; i <= end_y; i++) {


                let obj=checkIfIn(new Coordenates(start_x, i));

                if (obj!=false) {

                    addValue(obj);

                }

                else {

                    entries.push(new Coordenates(start_x,i));

                }

            }




            


        }

    }

    else if (start_y == end_y) {

        if (start_x > end_x) {

            for (let i = end_x; i <= start_x; i++) {

                let obj=checkIfIn(new Coordenates(i, start_y));

                if (obj!=false) {

                    addValue(obj);

                }

                else {

                    entries.push(new Coordenates(i,start_y));

                }

            }


        }

        else {


            for (let i = start_x; i <= end_x; i++) {

               

                    let obj=checkIfIn(new Coordenates(i, start_y));
    
                    if (obj!=false) {
    
                        addValue(obj);
    
                    }
    
                    else {
    
                        entries.push(new Coordenates(i,start_y));
    
                    }
    
                


            }


        }

    }


    //console.log(`start ${start} end ${end}\n`);

}

function fillEntriesDiagonal(start_x, start_y, end_x, end_y) {

    if (start_x == end_x) {

        if (start_y > end_y) {

            for (let i = end_y; i <= start_y; i++) {


                let obj=checkIfInDiagonal(new Coordenates(start_x, i));

                if (obj!=false) {

                    addValueDiagonal(obj);

                }

                else {

                    entriesDiagonal.push(new Coordenates(start_x,i));

                }

            }


        }

        else {

            for (let i = start_y; i <= end_y; i++) {


                let obj=checkIfInDiagonal(new Coordenates(start_x, i));

                if (obj!=false) {

                    addValueDiagonal(obj);

                }

                else {

                    entriesDiagonal.push(new Coordenates(start_x,i));

                }

            }




            


        }

    }

    else if (start_y == end_y) {

        if (start_x > end_x) {

            for (let i = end_x; i <= start_x; i++) {

                let obj=checkIfInDiagonal(new Coordenates(i, start_y));

                if (obj!=false) {

                    addValueDiagonal(obj);

                }

                else {

                    entriesDiagonal.push(new Coordenates(i,start_y));

                }

            }


        }

        else {


            for (let i = start_x; i <= end_x; i++) {

               

                    let obj=checkIfInDiagonal(new Coordenates(i, start_y));
    
                    if (obj!=false) {
    
                        addValueDiagonal(obj);
    
                    }
    
                    else {
    
                        entriesDiagonal.push(new Coordenates(i,start_y));
    
                    }
    
                


            }


        }

    }
    else if(start_x<end_x && start_y<end_y){


        //DIAGONAL IZQ ARRIBA

        let x=end_x;
        let y=end_y;

        
        while (x>=start_x){
            
            let obj=checkIfInDiagonal(new Coordenates(x,y));

            if (obj!=false) {
    
                addValueDiagonal(obj);

            }

            else {

                entriesDiagonal.push(new Coordenates(x,y));

            }

            x-=1;
            y-=1;
    
            


        }


    }

    else if(start_x>end_x && start_y<end_y){

        //DIAGONAL DER ARRIBA
        let x=end_x;
        let y=end_y;

        while (x<=start_x){

            
            let obj=checkIfInDiagonal(new Coordenates(x,y));

            if (obj!=false) {
    
                addValueDiagonal(obj);

            }

            else {

                entriesDiagonal.push(new Coordenates(x,y));

            }

            x+=1;
            y-=1;
    
            


        }

    }

    else if(start_x<end_x && start_y>end_y){

        //DIAGONAL IZQ ABAJO


        let x=end_x;
        let y=end_y;

        while (y<=start_y){

            
            let obj=checkIfInDiagonal(new Coordenates(x,y));

            if (obj!=false) {
    
                addValueDiagonal(obj);

            }

            else {

                entriesDiagonal.push(new Coordenates(x,y));

            }

            x-=1;
            y+=1;
    
            


        }

    }

    else if(start_x>end_x && start_y>end_y){

        //DIAGONAL DER ABAJO


        let x=end_x;
        let y=end_y;

        while (y<=start_y){

            
            let obj=checkIfInDiagonal(new Coordenates(x,y));

            if (obj!=false) {
    
                addValueDiagonal(obj);

            }

            else {

                entriesDiagonal.push(new Coordenates(x,y));

            }

            x+=1;
            y+=1;
    
            


        }


    }

}

function checkResult() {


    let counter = 0;

    for(let i=0;i<entries.length;i++){

        if (entries[i].value >= 2){

            counter += 1;

        }

    }


    return counter;

}

function checkResultDiagonal() {


    let counter = 0;

    for(let i=0;i<entriesDiagonal.length;i++){

        if (entriesDiagonal[i].value >= 2){

            counter += 1;

        }

    }


    return counter;

}



var array = [];
var entries = [];
var entriesDiagonal=[];





readFile();

for (let line of array) {

    getEntries(line);
    
}


console.log(`Part 1: ${checkResult()} \n`);
console.log(`Part 2: ${checkResultDiagonal()} \n`);



