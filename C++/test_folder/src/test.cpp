#include <iostream>

using namespace std;

int power(int number, int power) {
    int helper = number;

    for (int i = 0; i < power; i++)
        number *= helper;

    return number;
}

int main() {
    int SIZE;
    cin >> SIZE;

    for (int i = 0; i < SIZE; i++) {
        int result = power(5, i);
        cout << result << " ";
    }

    return 0;
}