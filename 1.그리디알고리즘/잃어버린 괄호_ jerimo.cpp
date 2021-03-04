#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
#include <map>
#include <unordered_map> // hash_map은 사용하지 말라고 뜸
using namespace std;

int main() {
	ios::ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string str;
	cin >> str;
	list<int> num;
	list<char> ope;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '-' || str[i] == '+') {
			ope.push_back(str[i]);
		}
		else {
			// 숫자이면
			string number = "";
			while (str[i] >= '0' && str[i] <= '9') {
				number += str[i];
				i++;
			}
			i--;
			int realNum = 0;
			int k = 1;
			for (int j = number.length() - 1; j >= 0; j--) {
				realNum += (number[j] - '0') * k;
				k *= 10;
			}
			num.push_back(realNum);
		}
	}
	int rst = num.front();
	num.pop_front();
	bool flag = false;
	while (!ope.empty()) {
		char oper = ope.front();
		ope.pop_front();
		if (oper == '-') {
			flag = true;
		}

		if (flag == true) {
			rst -= num.front();
			num.pop_front();
		}
		else {
			rst += num.front();
			num.pop_front();
		}
	}
	cout << rst;

	return 0;
}