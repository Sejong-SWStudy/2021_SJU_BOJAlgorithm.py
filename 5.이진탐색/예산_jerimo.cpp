#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int n = 0;
long m = 0; // 10^6�� �Ѿ
vector<int> v;
long sum = 0; // �굵 long���� �����

void findCost() {
	// ��� 1: ������ �ּڰ����� �ִ񰪱��� ����Ž������ �� �˻�
	// ��� 2: �ּڰ��̾�� �ұ�? �߰������� �����Ұ� ������
	// �ٵ� ����Ž���� ã�°��ݾ�..

	// �ٸ� �ڵ带 ����, ����Ž���̱� �ѵ�, mid�� �������� �����ϰ�
	// �� ���� ���, ���� m�� ���ؼ� ����Ž��
	// �ٵ� ����Ž���ϴ� ������ v�ȿ��� 1�� ������Ű�鼭


	// 1 5 6 100 ���� 18�� ���ó��
	// �� ����� ������ �������� Ž���ϴϱ� �������ѵ�
	// Ŀ�� ��ġ�� �κ��� ����. 
	// m�� ������ �̺�Ž���� �ϸ� ���ؾ� ��Ȯ�ϰ� ���� �� ����


	int lo = 0;
	int hi = m;
	int mid = 0;
	int rst = 0;
	long long sum = 0;
	while (lo <= hi) {
		mid = (lo + hi) / 2;
		sum = 0;
		// mid���� �������� �� ������ ����غ�
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
		// ������ ���̹Ƿ� �� ���� ���Ұ� �ִ�
		printf("%d", v.back());
	}
	else {
		// ���� ���� ���Ѿ��� �ִ���
		findCost();
	}
	return 0;
}