#include <bits/stdc++.h>

typedef long double ldouble;

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;
        vector<int> l(n);
        for (int i = 0; i < n; ++i) cin >> l[i];

        map<int, int> d;
        for (const int& l_i: l) {
            if (d.find(l_i) == d.end()) d[l_i] = 0;
            ++d[l_i];
        }

        vector<int> dg2;
        for (const auto& kv: d) {
            if (kv.second > 1) dg2.push_back(kv.first);
            if (kv.second > 3) dg2.push_back(kv.first);
        }

        sort(begin(dg2), end(dg2));

        vector<ldouble> r(dg2.size() - 1);

        for (int i = 0; i < dg2.size() - 1; ++i) r[i] = ldouble(dg2[i + 1]) / dg2[i];

        int pos = min_element(begin(r), end(r)) - begin(r);

        cout << dg2[pos] << " " << dg2[pos] << " " << dg2[pos + 1] << " " <<  dg2[pos + 1] << "\n";
    }
    return 0;
}