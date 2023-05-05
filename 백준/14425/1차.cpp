#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main() {
	int n, m;
	string str;
	cin >> n >> m;
	vector<string> sets;
	vector<string> arr;
	int count = 0;
	
	for (int i = 0; i < n; i++) {
		cin >> str;
		sets.push_back(str);
	}	

	for (int i = 0; i < m; i++) {
		cin >> str;
		arr.push_back(str);
	}

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i] == sets[j])
				count++;
		}
	}

	cout << count << endl;

	return 0;
}