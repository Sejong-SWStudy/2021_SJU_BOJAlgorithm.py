#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int n = 0;
int c = 0;
vector<long long> v;

long long dist = 0;

void binary() {
	int lo = 1; // 수직선 범위의 시작과
	int hi = v[n - 1] - v[0]; // 끝
	// 그러니까 배열의 길이가 아닌 그 안에 들어있는 거리가 기준
	// 저번의 예산 문제에서도 배열의 길이로 접근했다가 틀렸었음
	int mid = 0;
	int cnt = 0;
	int gap = 0; // 간격
	while (lo <= hi) {
		mid = (hi + lo) / 2;
		// mid가 간격이 되는거임
		// 그래서 mid에 설치하고 mid만큼 떨어진 쪽에 또 설치
		// 설치하고 나면 거기서부터 다시 시작이니까 start를 v[i]로
		int start = v[0];
		cnt = 1; // 첫 번째 집에는 무조건 설치
		for (int i = 1; i < n; i++) {
			gap = v[i] - start;
			if (mid <= gap) {
				// 설치된 집에서부터 다음 설치까지의 gap이
				// mid보다 크거나 같아야함
				cnt++;
				start = v[i];
			}
		}
		if (cnt < c) {
			// 공유기 설치가 아직 안끝났으면 간격을 좁혀서 다시
			hi = mid - 1;
		}
		else {
			dist = mid;
			lo = mid + 1;
		}
	}
	return;
}

int main() {
	cin >> n >> c;
	long long x = 0;
	for (int i = 0; i < n; i++) {
		cin >> x;
		v.push_back(x);
	}
	sort(v.begin(), v.end());

	if (c == 2) {
		// c가 2이면 양 끝에 설치하는게 거리 최대
		cout << v[n - 1] - v[0];
	}
	else {
		binary();
		cout << dist;
	}

	return 0;
}