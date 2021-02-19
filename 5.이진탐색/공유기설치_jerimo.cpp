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
	int lo = 1; // ������ ������ ���۰�
	int hi = v[n - 1] - v[0]; // ��
	// �׷��ϱ� �迭�� ���̰� �ƴ� �� �ȿ� ����ִ� �Ÿ��� ����
	// ������ ���� ���������� �迭�� ���̷� �����ߴٰ� Ʋ�Ⱦ���
	int mid = 0;
	int cnt = 0;
	int gap = 0; // ����
	while (lo <= hi) {
		mid = (hi + lo) / 2;
		// mid�� ������ �Ǵ°���
		// �׷��� mid�� ��ġ�ϰ� mid��ŭ ������ �ʿ� �� ��ġ
		// ��ġ�ϰ� ���� �ű⼭���� �ٽ� �����̴ϱ� start�� v[i]��
		int start = v[0];
		cnt = 1; // ù ��° ������ ������ ��ġ
		for (int i = 1; i < n; i++) {
			gap = v[i] - start;
			if (mid <= gap) {
				// ��ġ�� ���������� ���� ��ġ������ gap��
				// mid���� ũ�ų� ���ƾ���
				cnt++;
				start = v[i];
			}
		}
		if (cnt < c) {
			// ������ ��ġ�� ���� �ȳ������� ������ ������ �ٽ�
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
		// c�� 2�̸� �� ���� ��ġ�ϴ°� �Ÿ� �ִ�
		cout << v[n - 1] - v[0];
	}
	else {
		binary();
		cout << dist;
	}

	return 0;
}