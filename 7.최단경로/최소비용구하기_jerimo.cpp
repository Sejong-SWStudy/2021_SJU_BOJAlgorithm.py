#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

int n = 0;
int m = 0;
vector<pair<int, int>> graph[1001]; // ���� �������� �� ������ ���Ϳ� ����
// pair�� ��Һ񱳴� ù ��° ���� �̷�����Ƿ� ����� ���� �ִ´�.

// ���ͽ�Ʈ�� �˰��� ��� == �׸��� + ���̳��� ���α׷���
int dijkstra(int start, int end) {
	int i = 0;
	priority_queue <pair<int, int>> que;
	// min ���� �̿��ؾ� �ϹǷ�, ����� ���������� �־��ش�.
	vector<int> dist(n + 1, 987654321);

	dist[start] = 0;
	que.push({ 0,start });

	while (!que.empty()) {
		int cost = -que.top().first;
		int index = que.top().second; // ���� ����� �Ÿ��� ���� ���� ��ȣ
		que.pop();
		if (dist[index] < cost) {
			continue;
		}
		for (int i = 0; i < graph[index].size(); i++) {
			int next = graph[index][i].second;
			int nextCost = graph[index][i].first + cost;
			
			if (dist[next] > nextCost) {
				dist[next] = nextCost;
				que.push({ -nextCost,next });
			}
		}
	}
	return dist[end];
}

int main() {
	scanf("%d %d", &n, &m);
	int start, end, cost = 0;
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &start, &end, &cost);
		graph[start].push_back({ cost, end });
	}
	scanf("%d %d", &start, &end);

	printf("%d", dijkstra(start, end));



	return 0;
}