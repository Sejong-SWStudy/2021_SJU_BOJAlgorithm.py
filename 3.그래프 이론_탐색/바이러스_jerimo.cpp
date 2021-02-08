#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
using namespace std;

bool find(vector<int> v, int x) {
	// 컴퓨터의 개수가 100개 이하이므로
	// 반복문을 통해 요소가 있는지 확인
	bool flag = false;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == x) {
			flag = true;
			break;
		}
	}
	return flag;
}

void rDFS(vector<int> *graph, int v, vector<int> *cnt) {
	if (graph[v].empty()) {
		// 연결된 정점이 더이상 없으면 재귀문 탈출
		return;
	}
	for (int i = 0; i < graph[v].size(); i++) {
		if (!find(*cnt, graph[v][i])) {
			// 바이러스에 걸리지 않았을 때만 삽입
			(*cnt).push_back(graph[v][i]);
			rDFS(graph, graph[v][i], cnt);
		}
	}
	return;
}

int main() {
	int v, e = 0;
	cin >> v >> e;
	// 변수의 개수만큼 배열을 동적으로 생성
	// 벡터(=list) 배열을 선언하여 v*e개의 행렬처럼 사용해 그래프를 표현
	vector<int> * graph = new vector<int>[v + 1];
	for (int i = 0; i < e; i++) {
		int from, to;
		cin >> from >> to;
		graph[from].push_back(to);
		graph[to].push_back(from);
	}
	
	vector<int> cnt; // 바이러스에 걸린 컴퓨터는 배열에 넣고 이후에 배열의 크기를 구한다
	rDFS(graph, 1, &cnt);
	cout << cnt.size() - 1;

	return 0;
}