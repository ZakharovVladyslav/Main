#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	// initializing path as string
	string path = "assets/input_data.txt";

	// creating input file stream variable input_file with path as path
	ifstream input_file(path);

	// creating variables for checking brackets	
	int open_brackets = 0, close_brackets = 0;

	// if input file isn't open, send following message
	if (!input_file.is_open())
		cout << "File is not open";
	else {
		char symbol;


		input_file >> symbol;

		while (input_file) {
			if (symbol == '{')
				open_brackets++;
			else if (symbol == ' }')
				close_brackets++;

			if (open_brackets > close_brackets || open_brackets < close_brackets)
				cout << "Brackets balance is violated";

			input_file >> symbol;
		}
	}

	input_file.close();

	ofstream output_file;
	output_file.open(path);

	if (open_brackets == 0 && close_brackets == 0)
		cout << "There are no brackets in code";

	else if (open_brackets == close_brackets)
		cout << "Brackets balance isn't violated";

	return 0;

}