#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int minH = 1, maxH = 1e6;

vector<int> minTree, maxTree, h;
int n, k;

void buildMinTree(int v, int tl, int tr) {
	if (tl == tr)
		minTree[v] = h[tl];
	else {
		int tm = (tl + tr) >> 1;
		buildMinTree(v << 1, tl, tm);
		buildMinTree((v << 1) + 1, tm + 1, tr);
		minTree[v] = min(minTree[v << 1], minTree[(v << 1) + 1]);
	}
}

void buildMaxTree(int v, int tl, int tr) {
	if (tl == tr)
		maxTree[v] = h[tl];
	else {
		int tm = (tl + tr) >> 1;
		buildMaxTree(v << 1, tl, tm);
		buildMaxTree((v << 1) + 1, tm + 1, tr);
		maxTree[v] = max(maxTree[v << 1], maxTree[(v << 1) + 1]);
	}
}

int findMinTree(int v, int tl, int tr, int l, int r) {
	if (l > r)
		return maxH + 1;
	
	if (l == tl && r == tr)
		return minTree[v];
	
	int tm = (tl + tr) >> 1;
	
	return min(
		findMinTree(v << 1, tl, tm, l, min(tm, r)), 
		findMinTree((v << 1) + 1, tm + 1, tr, max(l, tm + 1), r)
	);
}

int findMaxTree(int v, int tl, int tr, int l, int r) {
	if (l > r)
		return minH - 1;
	
	if (l == tl && r == tr)
		return maxTree[v];
	
	int tm = (tl + tr) >> 1;
	
	return max(
		findMaxTree(v << 1, tl, tm, l, min(tm, r)), 
		findMaxTree((v << 1) + 1, tm + 1, tr, max(l, tm + 1), r)
	);
}

int binaryFind(int L, int l, int r) {
	if (l + 1 == r)
		return l;

	int m = (l + r) >> 1;

	if (findMaxTree(1, 0, n - 1, L, m) - findMinTree(1, 0, n - 1, L, m) <= k)
		return binaryFind(L, m, r);
	else
		return binaryFind(L, l, m);
}

int main() {
	cin >> n >> k;
	h.resize(n);
	minTree.resize(n << 2);
	maxTree.resize(n << 2);

	for (int i = 0; i < (n << 2); ++i) {
		maxTree[i] = minH - 1;
		minTree[i] = maxH + 1;
	}
	
	for (int i = 0; i < n; ++i) {
		cin >> h[i];
	}

	buildMinTree(1, 0, n - 1);
	buildMaxTree(1, 0, n - 1);

	int a = -1, b = 0;
	vector<int> p;

	for (int l = 0; l < n; ++l) {
		int r = binaryFind(l, l, n);

		if (r - l > a) {
			a = r - l;
			b = 1;
			p = {l};
		}
		else if (r - l == a) {
			b += 1;
			p.push_back(l);
		}
	}

	cout << a + 1 << ' ' << b << '\n';
	
	for (int i = 0; i < p.size(); ++i) {
		cout << p[i] + 1 << ' ' << p[i] + a + 1 << '\n';
	}

	return 0;
}
