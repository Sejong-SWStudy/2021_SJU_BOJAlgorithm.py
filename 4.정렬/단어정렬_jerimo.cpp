#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

class word {
	public:
		string num;
		int len;

		word(string _num) {
			num = _num;
			len = num.length();
		}
};

bool compare(word &a, word &b) {
	if (a.len < b.len)  return true;
	else if (a.len == b.len) { // 길이가 같으면
		if (a.num < b.num) return true;
		else return false;
	}
	else return false;
}

int main() {
	int n;
	cin >> n;
	getchar();
	string num;
	vector<word> v;
	set<string> s; // 중복 여부를 확인할 set
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (s.find(num) == s.end()) {
			v.push_back(word(num));
			s.insert(num);
		}
	}
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < v.size(); i++) {
		cout << v[i].num << '\n';
	}
	return 0;
}