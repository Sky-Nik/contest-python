#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <tuple>

typedef tuple<int, int> point;
typedef tuple<int, point> dp_elem;

inline int dist(point p1, point p2) {
	int x1 = get<0>(p1), y1 = get<1>(p1), x2 = get<0>(p2), y2 = get<1>(p2);
	return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

vector<dp_elem> dp;

int main() {
	int xs, ys;
	cin >> xs >> ys;
	point s = make_tuple(xs, ys);

	int n;
	cin >> n;

	vector<point> xyi(n);
	for (int i = 0; i < n; ++i) {
		int xi, yi;
		cin >> xi >> yi;
		xyi[i] = make_tuple(xi, yi);
	}

	dp.resize(n);
	dp[0] = make_tuple(0, make_tuple(-1, -1));
	for (int i = 1; i < (1 << n); ++i)
		dp[i] = make_tuple(1e9, make_tuple(-1, -1));

	for (int i = 0; i < (1 << n) - 1; ++i) {
		string s = bitset<n>(i).to_string();
		reverse(begin(s), end(s));
		// TODO
	}


	return 0;
}
