#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

class point {
public: 
	int x;
	int y;
	point() {
		x = 0;
		y = 0;
	}
	point(int _x, int _y) {
		x = _x;
		y = _y;
	}

	bool operator==(const point &p) {
		if (this->x == p.x &&this->y == p.y) {
			return true;
		}
		else return false;
	}
};

int main() {
	int n = 0;
	int k = 0;
	int r = 0;
	int c = 0;
	int apple[101][101] = { 0 }; // 1이면 사과 존재
	cin >> n >> k;
	for (int i = 0; i < k; i++) {
		cin >> r >> c;
		apple[r][c] = 1;
	}
	int l = 0;
	cin >> l;
	int X = 0;
	char C = 0;
	vector<pair<int, char>> v;
	for (int i = 0; i < l; i++) {
		cin >> X >> C;
		v.push_back({ X,C });
	}


	int sec = 0;
	int x = 1;
	int y = 1;
	int dx = 0;
	int dy = 1;
	vector<point> dist(4); // 방향을 담아둔 배열
	dist[0] = point(0, 1);
	dist[1] = point(1, 0);
	dist[2] = point(0, -1);
	dist[3] = point(-1, 0);
	int distN = 0; // 방향을 설정할 인덱스
	int order = 0; // 명령어 개수를 카운트


	list<point> dum; // 뱀의 위치를 표시할 배열

	dum.push_front(point(x, y));
	while (true) {
		sec++;
		x += dx;
		y += dy;
		// 게임 종료 여부를 판단
		if (x<1 || x>n || y < 1 || y > n) {
			// 벽에 닿았거나
			break;
		}
		if (find(dum.begin(), dum.end(), point(x, y)) != dum.end()) {
			// 자기 몸과 만났을때
			break;
		}

		// 새롭게 앞에 머리의 위치 삽입
		dum.push_front(point(x, y));
		if (apple[x][y] == 1) {
			// 사과를 먹었으면 없애고 꼬리 pop 안함
			apple[x][y] = 0;
		}
		else {
			// 가장 뒤에 있는게 꼬리이므로 
			dum.pop_back();
		}
		// 명령어를 확인하며 방향 전환
		if (order < l) {
			if (v[order].first == sec) {
				if (v[order].second == 'D') {
					distN++;
					if (distN > 3) {
						// 모듈러 연산
						distN -= 4;
					}
					dx = dist[distN].x;
					dy = dist[distN].y;
				}
				else {
					distN--;
					if (distN < 0) {
						// 모듈러 연산
						distN += 4;
					}
					dx = dist[distN].x;
					dy = dist[distN].y;
				}
				order++;
			}
		}
	}
	cout << sec;
	return 0;
}