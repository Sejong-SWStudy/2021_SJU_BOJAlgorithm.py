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
			// �� ��° ������ �±׺��ʹ� tmp�� ����� ���ڰ� ���� �� ����
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
				// ������ ������ tmp�� ����Ǿ� �ִ� ���ڵ� pop
				while (true) {
					if (tmp.empty()) {
						break;
					}
					char x = tmp.back();
					cout << x;
					tmp.pop_back();
				}
				if (s[i] != ' ') {
					// s[i] == '\0'�� ��� �ٷ� ����
					break;
				}
				else cout << s[i];
			}
			else tmp.push_back(s[i]);
		}
		else cout << s[i]; // flag�� true�� ��쿡�� �����
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