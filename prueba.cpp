#include <iostream>
#include<fstream>
#include<string>
#include <vector>

using namespace std;

vector<string> input;

void lectura()
{

    ifstream archivo;
    string texto;

    archivo.open("prueba.txt", ios::in);

    while (!archivo.eof())
    {

        getline(archivo, texto);
        input.push_back(texto);

        //height+=1;
        //cout<<texto<<endl;
    }

    //length=cave[0].size()-1;
    archivo.close();



}


int main(){

    lectura();
    int a=stoi(input[0]);
    cout << a<< endl;
    return 0;
}