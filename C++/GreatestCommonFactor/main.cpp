#include <iostream>

// Finding greatest common factor
// Number for test: 4851, 3003 = 231
int nod(int a, int b)
{
    /* At each step of the cycle, the remainder of dividing a by b is calculated
    then variable a is assigned the value of variable b
    variable b is assigned the remainder of dividing a by b
    the process stops when b = 0 */
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

int main(void)
{
    int a;
    int b;
    cout << "Enter number a: ";
    cin >> a;
    cout << "Enter number b: ";
    cin >> b;
    int out = nod(a, b);
    cout << "Result: " << out << endl;

    return 0;
}