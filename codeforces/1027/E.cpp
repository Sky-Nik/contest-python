#include <bits/stdc++.h>

typedef long long li;

using namespace std;

int main() {
	li mod = 998244353;

	int n, K;

	cin >> n >> K;

	int dp[2][507][507];
	for (int i = 0; i < 2; ++i)
		for (int j = 0; j <= n; ++j)
			for (int k = 0; k <= n; ++k)
				dp[i][j][k] = 0;

	dp[0][0][0] = 1;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= n; ++j)
			for (int k = 0; k <= n; ++k)
				dp[(i & 1) ^ 1][j][k] = 0;

		for (int j = 0; j < n; ++j) {
			for (int k = 0; k <= n; ++k) {
				dp[(i & 1) ^ 1][j + 1][max(k, j + 1)] += dp[i & 1][j][k];
				dp[(i & 1) ^ 1][j + 1][max(k, j + 1)] %= mod;
				dp[(i & 1) ^ 1][1][max(k, 1)] += dp[i & 1][j][k];
				dp[(i & 1) ^ 1][1][max(k, 1)] %= mod;
			}
		}
	}

	vector<li> cnt(n + 1, 0);

	for (int k = 0; k <= n; ++k) {
		for (int j = 0; j <= n; ++j) {
			cnt[k] += dp[n & 1][j][k];
			cnt[k] %= mod;
		}
	}

	vector<li> pr(n + 1, cnt[0]);

	for (int i = 1; i <= n; ++i) {
		pr[i] = pr[i - 1] + cnt[i];
		pr[i] %= mod;
	}

	li ans = 0;

	for (int i = 1; i <= n; ++i) {
		ans += cnt[i] * pr[min(n, (K - 1) / i)];
		ans %= mod;
	}

	ans = ans * ((mod + 1) / 2) % mod;

	cout << ans;

	return 0;
}