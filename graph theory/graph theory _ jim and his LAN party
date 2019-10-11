#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, int> pii;
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define eb emplace_back
#define fi first
#define pb push_back
#define se second

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 100000, LOGN = 17;
int dep[N], uf[N];
pii jp[LOGN][N];
vector<int> vs[N];
vector<pii> es[N];

void dfs(int d, int u, int p, int w)
{
  dep[u] = d;
  jp[0][u] = {p, w};
  for (auto &e: es[u])
    if (e.fi != p)
      dfs(d+1, e.fi, u, e.se);
}

int lca(int u, int v, int &mx)
{
  if (dep[u] < dep[v])
    swap(u, v);
  ROF(i, 0, LOGN)
    if (1 << i <= dep[u]-dep[v]) {
      mx = max(mx, jp[i][u].se);
      u = jp[i][u].fi;
    }
  if (u == v)
    return u;
  ROF(i, 0, LOGN)
    if (jp[i][u].fi != jp[i][v].fi) {
      mx = max(mx, jp[i][u].se);
      u = jp[i][u].fi;
      mx = max(mx, jp[i][v].se);
      v = jp[i][v].fi;
    }
  mx = max(mx, jp[0][u].se);
  mx = max(mx, jp[0][v].se);
  return jp[0][u].fi;
}

int find(int x)
{
  while (uf[x] != x)
    uf[x] = uf[uf[x]], x = uf[x];
  return x;
}

int main()
{
  int n = ri(), m = ri(), q = ri();
  REP(i, n)
    vs[ri()-1].pb(i);
  iota(uf, uf+n, 0);
  REP1(i, q) {
    int u = ri()-1, v = ri()-1, uu = find(u), vv = find(v);
    if (uu != vv) {
      uf[uu] = vv;
      es[u].eb(v, i);
      es[v].eb(u, i);
    }
  }
  fill_n(dep, n, -1);
  REP(i, n)
    if (dep[i] < 0)
      dfs(0, i, -1, 0);
  FOR(k, 1, LOGN)
    REP(i, n) {
      pii x = jp[k-1][i];
      jp[k][i] = ~ x.fi ? pii{jp[k-1][x.fi].fi, max(jp[k-1][x.fi].se, x.se)} : x;
    }
  REP(i, m) {
    int mx = 0;
    if (vs[i].size()) {
      int x = vs[i].back();
      vs[i].pop_back();
      while (vs[i].size()) {
        if (find(x) != find(vs[i].back())) {
          mx = -1;
          break;
        }
        x = lca(x, vs[i].back(), mx);
        vs[i].pop_back();
      }
    }
    printf("%d\n", mx);
  }
}
