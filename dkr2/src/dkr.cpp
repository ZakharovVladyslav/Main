#include <iostream>
#include <ctime>

using namespace std;

float calculating(float arr[], int SIZE) {
	float sum = 0;

	for (int i = 0; i < SIZE; i++)
		sum += arr[i];

	return sum;
}

int main() {
	srand((unsigned int)time(NULL));

	const int SIZE = 3;

	float arr[SIZE];

	for (int i = 0; i < SIZE; i++)
		arr[i] = rand() % 100 / 2.0; 

	cout << "Initial array: ";
	for (int i = 0; i < SIZE; i++)
		cout << arr[i] << " ";

	float res = calculating(arr, SIZE);

	cout << "\n\nresult: " << res << "\n";

	return 0;
}