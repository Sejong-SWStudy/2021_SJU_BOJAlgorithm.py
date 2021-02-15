#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

class house {
public:
	int num; // 집의 위치
	int distance; // 안테나로부터의 거리 합을 저장

	house(int _num) {
		num = _num;
		distance = 0;
	}
};

bool compare(house &a, house &b) {
	if (a.distance < b.distance) {
		return true;
	}
	else if (a.distance == b.distance) {
		return a.num < b.num;
	}
	else return false;
}

int main() {
	int n = 0;
	int x = 0;
	vector<house> v;
	scanf("%d", &n);
	for (int i = 0; i < n; i ++ ) {
		scanf("%d", &x);
		v.push_back(house(x));
	}
	/*for (int i = 0; i < n; i++) {
		int sum = 0;
		for (int j = 0; j < n; j++) {
			sum += abs(v[i].num - v[j].num);
		}
		v[i].distance = sum;
	}*/

	sort(v.begin(), v.end(), compare);
	printf("%d", v[(v.size()-1)/2].num);

	return 0;
}