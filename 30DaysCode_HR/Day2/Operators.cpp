#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;
int main(){
    double n = 0.0;
    int t1 = 0;
    int t2 = 0;
    string ws;
    double total;

    cin >> n;
    getline(cin, ws);
    cin >> t1;
    getline(cin, ws);
    cin >> t2;
    getline(cin, ws);

    total = n+ n*t1/100 +n*t2/100;
    cout << "The total meal cost is "<<int(round(total))<<" dollars."<<endl;

    return 0;
}