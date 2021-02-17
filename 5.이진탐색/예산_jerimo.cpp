#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int n = 0;
long m = 0; // 10^6을 넘어감
vector<int> v;
long sum = 0; // 얘도 long으로 잡아줌

void findCost() {
	// 방법 1: 예산의 최솟값부터 최댓값까지 이진탐색으로 다 검사
	// 방법 2: 최솟값이어야 할까? 중간값부터 가능할거 같은데
	// 근데 이진탐색은 찾는거잖아..

	// 다른 코드를 보니, 이진탐색이긴 한데, mid를 예산으로 생각하고
	// 그 합을 계산, 합을 m과 비교해서 이진탐색
	// 근데 이진탐색하는 범위가 v안에서 1씩 증가시키면서


	// 1 5 6 100 예산 18인 경우처럼
	// 내 방법은 예산을 기준으로 탐색하니까 빠르긴한데
	// 커버 못치는 부분이 존재. 
	// m을 가지고 이분탐색을 하며 구해야 정확하게 구할 수 있음


	int lo = 0;
	int hi = m;
	int mid = 0;
	int rst = 0;
	long long sum = 0;
	while (lo <= hi) {
		mid = (lo + hi) / 2;
		sum = 0;
		// mid값을 기준으로 총 예산을 계산해봄
		for (int i = 0; i < n; i++) {
			if (v[i] <= mid) {
				sum += v[i];
			}
			else sum += mid;
		}

		if (sum <= m) {
			rst = mid;
			lo = mid + 1;
		}
		else {
			hi = mid - 1;
		}
	}

	cout << rst;
	return;
}

int main() {
	cin >> n;
	int x = 0;
for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		v.push_back(x);
		sum += x;
	}
	cin >> m;
	sort(v.begin(), v.end());
	if (sum <= m) {
		// 정렬한 뒤이므로 맨 뒤의 원소가 최댓값
		printf("%d", v.back());
	}
	else {
		// 계산된 정수 상한액이 최댓값임
		findCost();
	}
	return 0;
}