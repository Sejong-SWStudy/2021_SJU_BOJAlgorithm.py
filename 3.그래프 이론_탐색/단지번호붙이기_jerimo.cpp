#include <iostream>

#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
using namespace std;

int n = 0; // 5 <= n <= 25
int ar[26][26] = { 0 };
int v[26][26] = { 0 }; // Ž�� ���θ� Ȯ���� �迭
int cnt = 0;

void rDFS(int i, int j) {
	if (i < 0 || i >= n || j < 0 || j >= n) {
		return; // ���� �Ѿ�� ����
	}
	if (ar[i][j] == 1 && v[i][j] == 0) {
		v[i][j] = 1;
		cnt++;
		// �����¿츦 Ȯ��
		rDFS(i + 1, j);
		rDFS(i, j + 1);
		rDFS(i - 1, j);
		rDFS(i, j - 1);
	}
}

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &ar[i][j]); // cin���δ� ������ ������ ����� ���� �ȵ�
		}
	}

	list<int> li; // ���� �� ���� ��
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (ar[i][j] == 1) {
				rDFS(i, j);
				if (cnt != 0) {
					li.push_back(cnt);
					cnt = 0;
				}
			}
		}
	}

	li.sort();
	cout << li.size() << '\n';
	int size = li.size();
	for (int i = 0; i < size; i++) {
		cout << li.front() << '\n';
		li.pop_front();
	}

	return 0;
}