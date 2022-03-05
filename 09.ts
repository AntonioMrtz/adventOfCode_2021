import { readFileSync } from 'fs';

function readFile(): string {

    let file = readFileSync('prueba.txt', 'utf-8');
    //let file = readFileSync('prueba.txt', 'utf-8');

    return file;

}

class Coordenates{

    constructor(i:number,j:number){

        this.i=i;
        this.j=j;
    }

    i:number;
    j:number;
    

}

function checkNearPoints(matrix: number[][], i: number, j: number): number {

    let currentHeight: number = matrix[i][j];


    if (i + 1 < matrix.length) {

        if (matrix[i + 1][j] <= currentHeight) {

            return -1;
        }

    }
    if (i > 0) {

        if (matrix[i - 1][j] <= currentHeight) {

            return -1;
        }

    }
    if (j + 1 < matrix[i].length) {

        if (matrix[i][j + 1] <= currentHeight) {

            return -1;
        }

    }
    if (j > 0) {

        if (matrix[i][j - 1] <= currentHeight) {

            return -1;
        }
    }

    let  coordenates:Coordenates=new Coordenates(i,j); 
    lowestPoints.push(coordenates);
    return currentHeight;
}

function findLowPoints(matrix: number[][]): number {


    let counter: number = 0;


    for (let i = 0; i < matrix.length; i++) {

        for (let j = 0; j < matrix[i].length; j++) {

            let aux: number = checkNearPoints(matrix, i, j);


            if (aux != -1) {
                
                aux = aux + 1;
                counter += aux;
            }
        }


    }


    return counter;
}


function mainP1(file: string): number {
    
    let data: Array<string> = file.split("\n");
    
    var matrix: number[][] = [];
    
    
    let i: number = 0;
    for (let line of data) {

        line = line.trim();

        let j: number = 0;
        matrix[i] = [];
        
        for (let height of line) {
            
            matrix[i][j] = parseInt(height);
            j++;
        }
        
        i++;
        
    }
    
    
    return findLowPoints(matrix);
    
    
}

function findBasin(i:number,j:number){ // returns size of basin

    //* LISTA DONDE HEMOS PASADO YA


    //* SI NO HEMOS PASADO ANTERIORMENTE Y !=9 -> CONTADOR+1
    //* CHECKEAR PROPIA CASILLA Y LANZAR EN 4 DIRECCIONES
    //* SI 9 ACABAR
    //* SI BORDE , LANZAR EN DIRECCIONES POSIBLES
    //* LANZAMOS ESTO DESDE CADA PUNTO BAJO


    return 0;
}

function getBiggestBasins(matrix:Array<number>[]){ 

    let basins:Array<number>=[];

    for(let coordenate of lowestPoints){

        basins.push(findBasin(coordenate.i,coordenate.j));

    }

    basins.sort();
    return basins[basins.length-1]+basins[basins.length-2]+basins[basins.length-3];

}


function mainP2(file: string): number{

    let data: Array<string> = file.split("\n");

    var matrix: number[][] = [];


    let i: number = 0;
    for (let line of data) {

        line = line.trim();

        let j: number = 0;
        matrix[i] = [];

        for (let height of line) {

            matrix[i][j] = parseInt(height);
            j++;
        }

        i++;

    }

    return getBiggestBasins(matrix);

}

const file = readFile();

var visited:Array<Coordenates>=[];
var lowestPoints:Array<Coordenates>=[];
console.log(`Part 1: ${mainP1(file)}\n`)
console.log(`Part 2: ${mainP2(file)}\n`)