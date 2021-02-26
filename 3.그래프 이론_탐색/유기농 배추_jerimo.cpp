#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
#include <unordered_map> // hash_map은 사용하지 말라고 뜸
using namespace std;

int n, m = 0;
vector<vector<int>> map(51, vector<int>(51)); // 50*50 배열 생성
vector<vector<int>> visit(51, vector<int>(51));
int cnt = 0;
void rDFS(int i, int j) {
	if (i < 0 || i >= n || j < 0 || j >= m) {
		return;
	}
	
	if (map[i][j] == 1 && visit[i][j] != 1) {
		visit[i][j] = 1;
		cnt++;
		rDFS(i - 1, j);
		rDFS(i + 1, j);
		rDFS(i, j - 1);
		rDFS(i, j + 1);
	}
}

int find() {
	int rst = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 1) {
				rDFS(i, j);
				// 한 무리를 셀 때마다 카운트
				if (cnt != 0) {
					rst++;
				}
				cnt = 0;
			}
		}
	}
	return rst;
}

void clear() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			map[i][j] = 0;
			visit[i][j] = 0;
		}
	}
	return;
}

int main() {
	ios::ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t = 0;

	int k = 0;
	int x, y = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> m >> n >> k;
		for (int j = 0; j < k; j++) {
			cin >> y >> x;
			map[x][y] = 1;
		}
		cout << find() << "\n";
		clear();
		cnt = 0;
	}

	return 0;
}