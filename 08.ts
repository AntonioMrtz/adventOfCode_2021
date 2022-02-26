import { readFileSync } from 'fs';

function readFile():string{
    
    let file = readFileSync('input08.txt', 'utf-8');
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

    let expectedResult:Array<number>=[1,4,7,8];
    
    for(let line of data){

        counter+=identifySelectedNumbers(line.split("|")[1]);

    }


    return counter;
}

const file=readFile();
console.log(`Part 1: ${mainP1(file)}\n`)

