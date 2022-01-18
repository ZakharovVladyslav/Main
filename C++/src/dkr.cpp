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

	if (pow < 0)
		pow = 1 / pow;

	if (pow == 0)
		n = 1;

	for (int i = 1; i < pow; i++)
		n *= k;

	return n;
}

int main() {
	unsigned int N;

	cout << "N: ";
	cin >> N;

	for (int n = 0; n < N; ++n) {		
		int res = power((-1), n) * (power(2, n) / factorial(n));

		cout << n + 1 << ": " << res << "\n";
	}

	return 0;
}