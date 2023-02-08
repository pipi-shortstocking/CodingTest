#include <iostream>

//길이가 30인 배열 선언(0으로 초기화)
//인덱스 번호 + 1와 일치하는 값을 각 요소로 할당
//배열을 훑으며 0인 값의 인덱스 번호 + 1 출력

using namespace std;

int main() {
	int arr[30] = { 0, };
	int num = 0;

	for (int i = 0; i < 28; i++) {
		cin >> num;
		arr[num-1] = num;
	}

	for (int i = 0; i < 30; i++) {
		if (arr[i] == 0) {
			cout << i + 1 << endl;
		}
	}
	
	return 0;
}
