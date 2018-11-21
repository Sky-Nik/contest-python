#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int sa(int l, int r) {
	if (r < 0)
		return sa(1 - r, 1 - l);
	else if (l < 0)
		return sa(0, 1 - l) + sa(0, r);
	else
		return (l + r - 1) * (r - l) / 2;
}

int main() {
	int n, k;
	cin >> n >> k;

	vector<int> m(n);
	for (size_t i = 0; i < n; ++i) cin >> m[i];
	
	int xc = k / 2, yc = k / 2;

	vector<vector<bool>> used(k, vector<bool>(k, false));

	for (int i = 0; i < n; ++i) {
		int x_o = -1, y_o = -1, d_o = 1e9;

		for (int x = 0; x < k; ++x) {
			for (int y = 0; y < k - m[i] + 1; ++y) {
				bool possible = true;
				for (int y1 = y; y1 < y + m[i]; ++y1) if (used[x][y1]) possible = false;

				if (possible) {
					int d = m[i] * abs(x - xc) + sa(y - yc, y + m[i] - yc);
					if (d < d_o) {
						x_o = x;
						y_o = y;
						d_o = d;
					}
				}
			}
		}

		if (x_o == -1) cout << "-1\n";
		else {
			for (int y = y_o; y < y_o + m[i]; ++y) used[x_o][y] = true;
			cout << x_o + 1 << ' ' << y_o + 1 << ' ' << y_o + m[i] << '\n';
		}
	}

	return 0;
}