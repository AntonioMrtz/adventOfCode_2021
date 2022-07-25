#include <iostream>
#include<fstream>
#include<string>
#include <vector>

using namespace std;

struct node{

    int x;
    int y;

};


vector<string> cave;


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
    
    int path_matrix[length+1][height+1];


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

    for(int j=1;j<height;j++){

        for(int i=1;i<length;i++){
        
            path_matrix[j][i]=(cave[j][i]-'0')+min(path_matrix[j-1][i],path_matrix[j][i-1]);

            
        }

        
    }


    // then we fill the cells that can have to ways

    for(int i=0;i<length;i++){

        for(int j=0;j<height;j++){
        


            cout << path_matrix[i][j]<<" ";
        }

        cout<<endl;
    }
    
    best_risk=path_matrix[height-1][length-1]-1; // -1 because you dont want to count first step ( always 1)

}


void part_1(){


    cout<<"heigth: "<<height<<" length: "<<length<<endl;

    
   
    fill_path_matrix();

    cout<<"best risk : "<<best_risk<<endl;

}

int main(){

    lectura();

    part_1();

    return 0;

}