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
	int apple[101][101] = { 0 }; // 1�̸� ��� ����
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
	vector<point> dist(4); // ������ ��Ƶ� �迭
	dist[0] = point(0, 1);
	dist[1] = point(1, 0);
	dist[2] = point(0, -1);
	dist[3] = point(-1, 0);
	int distN = 0; // ������ ������ �ε���
	int order = 0; // ��ɾ� ������ ī��Ʈ


	list<point> dum; // ���� ��ġ�� ǥ���� �迭

	dum.push_front(point(x, y));
	while (true) {
		sec++;
		x += dx;
		y += dy;
		// ���� ���� ���θ� �Ǵ�
		if (x<1 || x>n || y < 1 || y > n) {
			// ���� ��Ұų�
			break;
		}
		if (find(dum.begin(), dum.end(), point(x, y)) != dum.end()) {
			// �ڱ� ���� ��������
			break;
		}

		// ���Ӱ� �տ� �Ӹ��� ��ġ ����
		dum.push_front(point(x, y));
		if (apple[x][y] == 1) {
			// ����� �Ծ����� ���ְ� ���� pop ����
			apple[x][y] = 0;
		}
		else {
			// ���� �ڿ� �ִ°� �����̹Ƿ� 
			dum.pop_back();
		}
		// ��ɾ Ȯ���ϸ� ���� ��ȯ
		if (order < l) {
			if (v[order].first == sec) {
				if (v[order].second == 'D') {
					distN++;
					if (distN > 3) {
						// ��ⷯ ����
						distN -= 4;
					}
					dx = dist[distN].x;
					dy = dist[distN].y;
				}
				else {
					distN--;
					if (distN < 0) {
						// ��ⷯ ����
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