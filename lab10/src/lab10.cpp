#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

double max(double a, double b, double c) {
    return max(max(a, b), c);
}

int main() {
    ifstream input_data;
    input_data.open("assets/input_data.txt");

    if (!input_data.is_open()) {
        cout << "Error while opening file";
        system("pause");
        return 0;
    }

    int SIZE;
    input_data >> SIZE;

    double** arr = new double* [SIZE];
    for (int i = 0; i < SIZE; i++)
        arr[i] = new double[SIZE];

    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            input_data >> arr[i][j];


    double max_value = max(arr[0][0], arr[1][0], arr[2][0]);

    ofstream output_data;
    output_data.open("assets/output_data.txt");

    if (!output_data.is_open()) {
        cout << "Error while opening file";
        system("pause");
        return 0;
    }
    else {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                output_data << setprecision(3) << fixed << arr[i][j] / max_value << " ";
            }
            output_data << endl;
        }
    }

    for (int i = 0; i < SIZE; i++)
        delete[] arr[i];
    delete[] arr;

    input_data.close();
    output_data.close();

    return 0;
}