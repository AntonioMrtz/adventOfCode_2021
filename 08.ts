import { readFileSync } from 'fs';

function readFile(): string {

    let file = readFileSync('input08.txt', 'utf-8');

    return file;

}

function identifySelectedNumbers(outputLine: string): number {

    let counter: number = 0;

    outputLine = outputLine.trim();

    let outputs: Array<string> = outputLine.split(" ");

    let acceptedLengths: Array<number> = [2, 4, 3, 7];


    for (let output of outputs) {

        if (acceptedLengths.includes(output.length)) {

            counter++;
        }

    }


    return counter;

}

function mainP1(file: string): number {

    let counter: number = 0;
    let data: Array<string> = file.split("\n");

    for (let line of data) {

        counter += identifySelectedNumbers(line.split("|")[1]);

    }


    return counter;
}



function caseInsensitiveSort(a: string, b: string): number {
    var ret = 0;
    a = a.toLowerCase(); b = b.toLowerCase();
    if (a > b)
        ret = 1;
    if (a < b)
        ret = -1;
    return ret;
}


function checkLettersIn(input: string, expected: string) { // returns 0 if is contained and 1 if not 

    for (let i = 0; i < input.length; i++) {

        if (!expected.includes(input[i])) {

            return 1;
        }

    }

    return 0;

}

function countCoincidences(input: string, expected: string) { // returns number of coincidences 

    let counter: number = 0;

    for (let i = 0; i < input.length; i++) {

        if (expected.includes(input[i])) {

            counter++;
        }

    }

    return counter;

}

function getByValue(map: Map<number, string>, searchValue: string): number {


    for (let [key, value] of map.entries()) {

        if (value == searchValue) {
            return key;
        }
    }
    return -1;
}

function processOutput(map: Map<number, string>, output: string): number {

    let outputNumber: string = "";
    let outputArray: Array<string> = output.trim().split(" ");

    console.log(map);


    for (let out of outputArray) {

        out = out.split('').sort(caseInsensitiveSort).join('');
        outputNumber += getByValue(map, out);

    }


    //console.log(outputNumber);
    return parseInt(outputNumber);
}



function getNumbers(inputLine: string): Map<number, string> {

    let dict = new Map<number, string>();
    let postProcessed: Array<string> = [];

    inputLine = inputLine.trim();

    let inputs: Array<string> = inputLine.split(" ");



    for (let input of inputs) {


        switch (input.length) {

            case 2:
                dict.set(1, input.split('').sort(caseInsensitiveSort).join(''));
                break

            case 4:
                dict.set(4, input.split('').sort(caseInsensitiveSort).join(''));
                break

            case 3:
                dict.set(7, input.split('').sort(caseInsensitiveSort).join(''));
                break

            case 7:
                dict.set(8, input.split('').sort(caseInsensitiveSort).join(''));
                break

            case 6:

                postProcessed.push(input);
                break

            case 5:

                postProcessed.push(input);
                break

        }


    }

    //* LEN==5

    for (let input of postProcessed) {

        if (input.length == 5) {

            if (countCoincidences(dict.get(1)!, input) == 2) { //3

                dict.set(3, input.split('').sort(caseInsensitiveSort).join(''));

            }

            else {// 2 o 5

                if (countCoincidences(dict.get(4)!, input) == 2) {

                    dict.set(2, input.split('').sort(caseInsensitiveSort).join(''));
                }

                else {

                    dict.set(5, input.split('').sort(caseInsensitiveSort).join(''));
                }

            }

        }

    }


    //* LEN==6

    for (let input of postProcessed) {

        if (input.length == 6) {

            if (countCoincidences(dict.get(1)!, input) != 2) { //6

                dict.set(6, input.split('').sort(caseInsensitiveSort).join(''));

            }

            else { // 0 o 9

                if (countCoincidences(dict.get(4)!, input) == 4) {  // 9

                    dict.set(9, input.split('').sort(caseInsensitiveSort).join(''));
                }

                else {  // 0

                    dict.set(0, input.split('').sort(caseInsensitiveSort).join(''));
                }
            }


        }






    }


    return dict;
}












function mainP2(file: string): number {

    let counter: number = 0;
    let data: Array<string> = file.split("\n");

    let expectedResult: Array<number> = [1, 4, 7, 8];

    for (let line of data) {

        let map = getNumbers(line.split("|")[0]);
        counter += processOutput(map, line.split("|")[1]);

    }


    return counter;
}


const file = readFile();
console.log(`Part 1: ${mainP1(file)}\n`)
console.log(`Part 2: ${mainP2(file)}\n`)

