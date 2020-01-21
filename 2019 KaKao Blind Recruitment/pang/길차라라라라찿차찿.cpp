출처 : https://gist.github.com/fpdjsns/f74311db6bd5c563247cbac2bf210b7b

#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include<iostream>
#define MAX 1e5+1
using namespace std;

class Node { // 노드 형성
public:
	int value;
	Node* left = NULL;
	Node* right = NULL;
	Node(int value) { this->value = value; }
};


// y 내림차순 정렬
bool compare(vector<int>& a, vector<int>& b) { //2개의 백터 받아 정렬
	return a[1] == b[1] ? a[0] < b[0] : a[1] > b[1]; // 같은 레벨이면 더 작은 x가 앞으로, 다른 레벨이면 더 높게 있는 걸 먼저.
}

vector<priority_queue<pair<int, int>>> yList; //y를 인덱스로 하는 (-x, val) 우선순위큐를 저장한 배열
int depth = 0;

Node* makeBinaryTree(int maxX, int level) {//

	int x = -yList[level].top().first; //최우선순위 노드 반환
	int val = yList[level].top().second;
	yList[level].pop(); //퍽-발
	Node* root = new Node(val);

	// 마지막 레벨이거나 자식 노드들이 없으면
	// 자식 노드 세팅 필요없음.
	if (level == depth || yList[level + 1].empty()) //깊이와 같거나 더 윗 레벨이 없다면.
		return root;

	// 왼쪽 노드
	int nextX = -yList[level + 1].top().first;
	if (nextX < x)
		root->left = makeBinaryTree(x, level + 1);
	if(yList[level + 1].empty())
		return root;

	// 오른쪽 노드
	nextX = -yList[level + 1].top().first;
	if (x < nextX && nextX < maxX)
		root->right = makeBinaryTree(maxX, level + 1);
	return root;
}

vector<int> preOrder, postOrder;
void setPreOrder(Node* root) {
	if (root == NULL)
		return;
	preOrder.push_back(root->value);
	setPreOrder(root->left);
	setPreOrder(root->right);
}
void setPostOrder(Node* root) {
	if (root == NULL)
		return;
	setPostOrder(root->left);
	setPostOrder(root->right);
	postOrder.push_back(root->value);
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
	vector<vector<int>> answer;
	int beforeY = -1;
	for (int i = 0; i < nodeinfo.size(); i++) {
		nodeinfo[i].push_back(i + 1);//노드의 번호 추가
	}

	sort(nodeinfo.begin(), nodeinfo.end(), compare);//begin~ end 사이를 compare의 조건하에 정렬
	int ind = -1;
	for (int i = 0; i < nodeinfo.size(); i++) {
		int nowY = nodeinfo[i][1];
		if (nowY != beforeY) {
			ind++;
			yList.push_back(priority_queue<pair<int,int>>()); //레벨 다르면 끝에 추가.
			beforeY = nowY;
		}
		yList[ind].push({ -nodeinfo[i][0], nodeinfo[i][2]});
	}
	depth = ind;

	Node* root = makeBinaryTree(MAX, 0);
	setPreOrder(root); //전위
	setPostOrder(root);//후위
	answer.push_back(preOrder);
	answer.push_back(postOrder);
	return answer;
}
