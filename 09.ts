import { readFileSync } from 'fs';




function readFile(): string {

    //let file = readFileSync('prueba.txt', 'utf-8');
    let file = readFileSync('input09.txt', 'utf-8');

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

var size:number=0;


function checkCoordenates(i:number,j:number,array:Array<Coordenates>):boolean{

    for(let coordenate of array){

        if(coordenate.i==i && coordenate.j==j){

            return true;
        }

    }

    return false;
}

function findBasin(i:number,j:number,array:Array<Coordenates>,matrix:Array<number>[]){ // returns size of basin


    if(!checkCoordenates(i,j,array)){

        array.push(new Coordenates(i,j));  // ACTUALIZAMOS visitados

        if(matrix[i][j]!=9){ //* SI ES 9 NO PROPAGAMOS , en principio se deberia llegar desde otros nodos

            size++;

            // llamar todas direcciones

            if(i+1<matrix.length){

                findBasin(i+1,j,array,matrix); // ABAJO

            }

            if(i>0){

                findBasin(i-1,j,array,matrix); // ARRIBA

            }

            if(j>0){

                findBasin(i,j-1,array,matrix); // IZQUIERDA

            }

            if(j+1<matrix[i].length){

                findBasin(i,j+1,array,matrix); // DERECHA

            }


        }

    }

    //* SI NO HEMOS PASADO ANTERIORMENTE Y !=9 -> CONTADOR+1
    //* CHECKEAR PROPIA CASILLA Y LANZAR EN 4 DIRECCIONES
    //* SI 9 ACABAR
    //* SI BORDE , LANZAR EN DIRECCIONES POSIBLES
    //* LANZAMOS ESTO DESDE CADA PUNTO BAJO

}

function getBiggestBasins(matrix:Array<number>[]){ 

    let basins:Array<number>=[];

    for(let coordenate of lowestPoints){

        size=0;
        findBasin(coordenate.i,coordenate.j,[],matrix);
        basins.push(size);

    }

    basins.sort((n1,n2) => n1 - n2);
    //console.log(`areas : ${basins}`);
    return basins[basins.length-1]*basins[basins.length-2]*basins[basins.length-3];

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