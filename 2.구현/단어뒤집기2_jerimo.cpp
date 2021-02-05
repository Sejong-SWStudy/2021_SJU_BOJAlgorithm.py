#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
using namespace std;


int main() {

	string s;
	string tmp;
	bool flag = false;
	getline(cin, s);
	getchar();
	for (int i = 0; i < s.size() + 1; i++) {
		if (s[i] == '<') {
			flag = true;
			// 두 번째 이후의 태그부터는 tmp에 저장된 문자가 있을 수 있음
			while (true) {
				if (tmp.empty()) {
					break;
				}
				char x = tmp.back();
				cout << x;
				tmp.pop_back();
			}
			cout << s[i];
		}
		else if (s[i] == '>') {
			flag = false;
			cout << s[i];
		}
		else if (flag == false) {
			if (s[i] == ' ' || s[i] == '\0') {
				// 공백을 만나면 tmp에 저장되어 있던 문자들 pop
				while (true) {
					if (tmp.empty()) {
						break;
					}
					char x = tmp.back();
					cout << x;
					tmp.pop_back();
				}
				if (s[i] != ' ') {
					// s[i] == '\0'일 경우 바로 종료
					break;
				}
				else cout << s[i];
			}
			else tmp.push_back(s[i]);
		}
		else cout << s[i]; // flag가 true일 경우에만 실행됨
	}
	while (true) {
		if (tmp.empty()) {
			break;
		}
		int x = tmp.back();
		cout << x;
		tmp.pop_back();
	}
	cout << '\n';
	return 0;
}