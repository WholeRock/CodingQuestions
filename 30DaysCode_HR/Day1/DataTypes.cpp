#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
    // Declare second integer, double, and String variables.
    int i2 =0;
    double d2 = 0;
    string s2;
    string ws;

    // Read and save an integer, double, and String to your variables.
    cin >> i2;
    getline(cin, ws);
    cin >> d2;
    getline(cin,ws);
    getline(cin, s2);
    // Print the sum of both integer variables on a new line.
    cout << i+i2 <<endl;
    // Print the sum of the double variables on a new line.
    printf("%.1f\n",d+d2);

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s+s2 << endl;
    return 0;
}