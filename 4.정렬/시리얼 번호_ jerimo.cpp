#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
using namespace std;

class serial {
	public:
		string num;
		int len;
		int sum;

		serial(string _num) {
			num = _num;
			len = num.length();
			sum = 0;
			for (int i = 0; i < len; i++) {
				if (num[i] >= '0'&&num[i] <= '9') {
					sum += num[i] - '0';
				}
			}
		}
};

bool compare(serial &a, serial &b) {
	if (a.len < b.len)  return true;
	else if (a.len == b.len) { // 길이가 같으면
		if (a.sum < b.sum) { // 합이 작은게 먼저
			return true;
		}
		else if (a.sum == b.sum) { // 합이 같으면
			return a.num < b.num; // 사전순 비교
		}
		else return false;
	}
	else return false;
}

int main() {
	int n;
	cin >> n;
	getchar();
	string num;
	vector<serial> v;
	for (int i = 0; i < n; i++) {
		cin >> num;;
		v.push_back(serial(num));
	}
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < n; i++) {
		cout << v[i].num << '\n';
	}
	return 0;
}