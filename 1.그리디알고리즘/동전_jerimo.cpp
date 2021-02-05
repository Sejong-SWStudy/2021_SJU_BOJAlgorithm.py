#include <iostream>
#include <string>
#include <list>
#include <vector>
using namespace std;

int main() {
	int n, k = 0;
	cin >> n >> k;
	list<int> li;
	int x = 0;
	for (int i = 0; i < n; i++) {
		cin >> x;
		li.push_front(x); // 내림차순으로 리스트에 저장
	}

	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (k / li.front() > 0) {
			cnt += k / li.front();
			k = k % li.front();
		}
		li.pop_front();
	}
	cout << cnt;

	return 0;
}