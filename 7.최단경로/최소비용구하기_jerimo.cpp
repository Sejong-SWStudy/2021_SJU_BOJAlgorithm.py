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
vector<pair<int, int>> graph[1001]; // 비용과 도착지를 한 쌍으로 벡터에 담음
// pair의 대소비교는 첫 번째 부터 이루어지므로 비용을 먼저 넣는다.

// 다익스트라 알고리즘 사용 == 그리디 + 다이나믹 프로그래밍
int dijkstra(int start, int end) {
	int i = 0;
	priority_queue <pair<int, int>> que;
	// min 힙을 이용해야 하므로, 비용을 음수값으로 넣어준다.
	vector<int> dist(n + 1, 987654321);

	dist[start] = 0;
	que.push({ 0,start });

	while (!que.empty()) {
		int cost = -que.top().first;
		int index = que.top().second; // 가장 가까운 거리를 가진 정점 번호
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