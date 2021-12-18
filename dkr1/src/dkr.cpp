#include <iostream>

using namespace std;

int factorial(int n) {
	if (n == 0) 
		return 1;
	else 
		return n * factorial(n - 1);
}

int power(int n, int pow) {
	int k = n;

	for (int i = 1; i < pow; i++)
		n *= k;

	return n;
}

int main() {
	int a;
	unsigned int N;

	cout << "a: ";
	cin >> a;
	cout << "N: ";
	cin >> N;

	for (int n = 0; n < N; n++) {
		int res = (pow((-1), n))* (pow(2, n) / factorial(n));
		cout << res << " ";
	}

	return 0;
}