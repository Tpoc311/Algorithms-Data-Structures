#include <iostream>

// Finding greatest common factor
// Number for test: 4851, 3003 = 231
int greatest_common_factor(int a, int b)
{
    int remainder = 0;
    while (b != 0)
    {
        remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

using namespace std;

int main()
{
    int a;
    int b;
    cout << "Enter number a: ";
    cin >> a;
    cout << "Enter number b: ";
    cin >> b;
    int out = greatest_common_factor(a, b);
    cout << "Result: " << out << endl;

    return 0;
}