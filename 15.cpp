#include <iostream>
#include<fstream>
#include<string>
#include <vector>

/*https://www.youtube.com/watch?v=t1shZ8_s6jc*/
/* Made with dynamic programming */
/* Manhattan tourist problem */

using namespace std;

struct node{

    int x;
    int y;

};


vector<string> cave;
vector<string> big_cave;



int height=0;
int length=0;

int best_risk=0;



void lectura()
{

    ifstream archivo;
    string texto;

    archivo.open("input15.txt", ios::in);
    //archivo.open("prueba.txt", ios::in);


    while (!archivo.eof())
    {

        getline(archivo, texto);
        cave.push_back(texto);

        height+=1;
    }

    length=cave[0].size();
    archivo.close();



}
void fill_path_matrix(){

    // first we fill the top and left rows
    
    //int path_matrix[length+1][height+1];

    int path_matrix[length][height];



    path_matrix[0][0]=1;

    for(int i=0;i<length;i++){

        if(i!=0){

            path_matrix[0][i]=(path_matrix[0][i-1])+(cave[0][i]-'0');
            //cout << path_matrix[0][i-1]<< " "<<cave[0][i]-'0'<<" "<<path_matrix[0][i]<<endl;

        }

    }

    for(int i=0;i<height;i++){

        if(i!=0){

            path_matrix[i][0]=(path_matrix[i-1][0])+(cave[i][0]-'0');
            //cout << path_matrix[0][i-1]<< " "<<cave[0][i]-'0'<<" "<<path_matrix[0][i]<<endl;

        }

    }

    // then we fill the cells that can have to ways

    for(int j=1;j<height;j++){

        for(int i=1;i<length;i++){
        
            path_matrix[j][i]=(cave[j][i]-'0')+min(path_matrix[j-1][i],path_matrix[j][i-1]);

            
        }

        
    }



    /*for(int i=0;i<length;i++){

        for(int j=0;j<height;j++){
        


            cout << path_matrix[i][j]<<" ";
        }

        cout<<endl;
    }*/
    
    best_risk=path_matrix[height-1][length-1]-1; // -1 because you dont want to count first step ( always 1)

}


void part_1(){


    cout<<"heigth: "<<height<<" length: "<<length<<endl;

    
   
    fill_path_matrix();

    cout<<"best risk : "<<best_risk<<endl;

}


void make_new_cave(){


    vector<string> aux;

    for(int i=0;i<5*length;i++){


        big_cave.push_back("");
    }


    for(int times=0;times<5;times++){


        for(int times2=times;times2<times+5;times2++){

            // times2 tiene el incremento de la matriz
            // length tiene nº filas de una seccion

            vector<string> aux2;
            aux=aux2;

            for(int i=0;i<height;i++){

               
                aux.push_back("");

                for(int j=0;j<length;j++){
                
                    string num=to_string((cave[i][j]-'0')+times2);

                    if((atoi(num.c_str()))==10){

                        num="1";
                    }
                    else if((atoi(num.c_str()))>10){

                        num=to_string(atoi(num.c_str())-9);

                    }

                    aux[i]+=(num).c_str();

                
                }

                big_cave[times*height+i]=(big_cave[times*height+i]+aux[i]).c_str();

               
            }


        }


    }

     //*DEBUG BIG CAVE
    /*for(int i=0;i<5*length;i++){

        cout<<big_cave[i]<<endl;
    }*/



}


void part_2(){

    make_new_cave();

    cave=big_cave;
    length=length*5;
    height=height*5;

    cout<<"heigth: "<<height<<" length: "<<length<<endl;

    fill_path_matrix();

    cout<<"best risk : "<<best_risk<<endl;


}

int main(){

    lectura();

    part_1();

    part_2();

    return 0;

}