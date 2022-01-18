#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream input_data;
	input_data.open("../assets/input_data.txt");

	if (!input_data.is_open())
		cout << "Open error";

	int count_open_br = 0, count_close_br = 0;

	char symbol;

	while(input_data >> symbol) {
		if (symbol == '{')
			count_open_br++;
		else if (symbol == '}')
			count_close_br++;
	}

	
}