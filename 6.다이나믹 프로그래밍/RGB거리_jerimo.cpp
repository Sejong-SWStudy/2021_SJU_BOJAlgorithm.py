#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	cin >> n;
	int v[1001][3] = { 0 };
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &v[i][0], &v[i][1], &v[i][2]);
	}

	int dp[1001][3] = { 0 };
	// �� ���򺰷� ù ���� ��ĥ ����� �ְ�
	dp[0][0] = v[0][0];
	dp[0][1] = v[0][1];
	dp[0][2] = v[0][2];

	// ���� ���� �����̶�� �� �� ���� ������ �Ķ� �� �ʷ��� �ϳ�

	for (int i = 1; i < n; i++) {
		dp[i][0] = v[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
		dp[i][1] = v[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
		dp[i][2] = v[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
	}
	
	printf("%d", min(min(dp[n-1][0],dp[n-1][1]),dp[n-1][2]));
	return 0;
}