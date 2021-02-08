#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
using namespace std;

bool find(vector<int> v, int x) {
	// ��ǻ���� ������ 100�� �����̹Ƿ�
	// �ݺ����� ���� ��Ұ� �ִ��� Ȯ��
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
		// ����� ������ ���̻� ������ ��͹� Ż��
		return;
	}
	for (int i = 0; i < graph[v].size(); i++) {
		if (!find(*cnt, graph[v][i])) {
			// ���̷����� �ɸ��� �ʾ��� ���� ����
			(*cnt).push_back(graph[v][i]);
			rDFS(graph, graph[v][i], cnt);
		}
	}
	return;
}

int main() {
	int v, e = 0;
	cin >> v >> e;
	// ������ ������ŭ �迭�� �������� ����
	// ����(=list) �迭�� �����Ͽ� v*e���� ���ó�� ����� �׷����� ǥ��
	vector<int> * graph = new vector<int>[v + 1];
	for (int i = 0; i < e; i++) {
		int from, to;
		cin >> from >> to;
		graph[from].push_back(to);
		graph[to].push_back(from);
	}
	
	vector<int> cnt; // ���̷����� �ɸ� ��ǻ�ʹ� �迭�� �ְ� ���Ŀ� �迭�� ũ�⸦ ���Ѵ�
	rDFS(graph, 1, &cnt);
	cout << cnt.size() - 1;

	return 0;
}