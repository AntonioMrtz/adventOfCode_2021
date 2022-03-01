import { readFileSync } from 'fs';

function readFile():string{
    
    //let file = readFileSync('input08.txt', 'utf-8');
    let file = readFileSync('prueba.txt', 'utf-8');

    return file;

}

function identifySelectedNumbers(outputLine:string):number{

    let counter:number=0;

    outputLine=outputLine.trim();

    let outputs:Array<string>=outputLine.split(" ");

    let acceptedLengths:Array<number>=[2,4,3,7];


    for(let output of outputs){

        if(acceptedLengths.includes(output.length)){

            counter++;
        }
        
    }


    return counter;

}

function mainP1(file:string):number {

    let counter:number=0;
    let data:Array<string> =file.split("\n");
    
    for(let line of data){

        counter+=identifySelectedNumbers(line.split("|")[1]);

    }


    return counter;
}



function caseInsensitiveSort(a:string, b:string):number
{
   var ret = 0;
   a = a.toLowerCase();b = b.toLowerCase();
   if(a > b)
      ret = 1;
   if(a < b)
      ret = -1;
   return ret;
}

function getNumbers(inputLine:string):Map<number,string>{

    let dict=new Map<number,string>();

    inputLine=inputLine.trim();

    let inputs:Array<string>=inputLine.split(" ");

    for(let input of inputs){


        switch(input.length){

            case 1:
                dict.set(input.length,input.split('').sort(caseInsensitiveSort).join(''));

            case 4:
                dict.set(input.length,input.split('').sort(caseInsensitiveSort).join(''));
            
            case 7:
                dict.set(input.length,input.split('').sort(caseInsensitiveSort).join(''));

            case 8:
                dict.set(input.length,input.split('').sort(caseInsensitiveSort).join(''));

            //TODO 0,2,3,5,6,9
            //TODO MIRAR CON RESPECTO A FIJAS , substrings

        }

        
    }
    
    console.log(dict);

    return dict;
}

function processOutput(map:Map<number,string>,output:string):number{



    return 0;
}







function mainP2(file:string):number {

    let counter:number=0;
    let data:Array<string> =file.split("\n");

    let expectedResult:Array<number>=[1,4,7,8];
    
    for(let line of data){

        let map=getNumbers(line.split("|")[0]);
        counter+=processOutput(map,line.split("|")[0]);

    }


    return counter;
}


const file=readFile();
console.log(`Part 1: ${mainP1(file)}\n`)
console.log(`Part 2: ${mainP2(file)}\n`)

