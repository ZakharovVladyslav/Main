#include <iostream>
#include <fstream>

using namespace std;

int main() {

	ifstream input_data;
	input_data.open("../assets/input_data.txt");

	if (!input_data.is_open())
		cout << "Open error\n";

	int SIZE;
	input_data >> SIZE;

	int** arr1 = new int* [SIZE];
	for (int i = 0; i < SIZE; i++)
		arr1[i] = new int[SIZE];

	int** arr2 = new int* [SIZE];
	for (int i = 0; i < SIZE; i++)
		arr2[i] = new int[SIZE];

	for (int i = 0; i < SIZE; i++)
		for (int j = 0; j < SIZE; j++)
			input_data >> arr1[i][j];

	for (int i = 0; i < SIZE; i++)
		for (int j = 0; j < SIZE; j++)
			input_data >> arr2[i][j];

	int** arr3 = new int* [SIZE];
	for (int i = 0; i < SIZE; i++)
		arr3[i] = new int[SIZE];

	for (int i = 0; i < SIZE; i++)
		for (int j = 0; j < SIZE; j++)
			arr3[i][j] = arr1[i][j] + arr2[i][j];

	ofstream output_data;
	output_data.open("../assets/output_data.txt");

	if (!output_data.is_open())
		cout << "Open error\n";

	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++)
			output_data << arr3[i][j] << " ";
		output_data << endl;
	}

	for (int i = 0; i < SIZE; i++)
		delete[] arr1[i];
	delete[] arr1;

	for (int i = 0; i < SIZE; i++)
		delete[] arr2[i];
	delete[] arr2;

	for (int i = 0; i < SIZE; i++)
		delete[] arr3[i];
	delete[] arr3;

	return 0;
}