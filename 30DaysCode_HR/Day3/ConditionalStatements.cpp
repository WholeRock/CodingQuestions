#include <iostream>
#include <stdio.h>

using namespace std;


int main(){
    int N;
    cin >> N;
    if(N%2 == 1){
        cout <<"Weird"<<endl;
    }else if(N >=6 && N <= 20){
        cout <<"Weird"<<endl;
    }else{
        cout <<"Not Weird"<<endl;
    }
    return 0;
}