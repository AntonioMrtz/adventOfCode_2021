import { readFileSync } from 'fs';

function readFile(): string {

    let file = readFileSync('input09.txt', 'utf-8');
    //let file = readFileSync('prueba.txt', 'utf-8');

    return file;

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

const file = readFile();
console.log(`Part 1: ${mainP1(file)}\n`)