#pragma GCC optimize("Ofast")
// #pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
using namespace std;
#define fastIO                      \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL);                    \
  cout.tie(NULL)
const int mxN = 1e5 + 10;
#define int long long
int32_t mod = 1e9 + 7;
#define MAX_N 100001
auto cmp = [](auto left, auto right)
{ return (right.first) < (left.first); }; // ascending
auto cmp2 = [](auto left, auto right)
{ return (left.first) < (right.first); }; // descending
#define pii pair<int, int>
#define rep(i, n) for (int i = 0; i < n; ++i)
#define repr(i, n) for (int i = n; i >= 0; i--)
#define repl(i, j, n) for (int i = j; i < n; ++i)
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// template<class T>
// using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;//find by order
// void Print(int32_t x) {cout << x << " ";} void Print(char x) {cout << x << " ";} void Print(const char *x) {cout << x << " ";} void Print(double x) {cout << x << " ";} void Print(int x) {cout << x << " ";} void print() {cout << endl;}
// void Print(bool x) {cout << (x ? "YES" : "NO");} void Print(const string &x) {cout << x << " ";}  template<typename T, typename V> void Print(const pair<T, V> x) {cout << x.first << " " << x.second << endl;}
// template<typename T> void Print(const T &x) {for (auto &i : x) Print(i);} template <typename T, typename... V> void print(T t, V... v) { Print(t); print(v...);}

long long binpow(long long a, long long b)
{
  long long res = 1;
  while (b > 0)
  {
    if (b & 1)
      res = res * a;
    a = a * a;
    b >>= 1;
  }
  return res;
}
const int LOG=20;
vector<int>depth(2e5+100,0);
vector<vector<int>>up(LOG,vector<int>(2e5+100,0)),g;

void dfs(int node,int parent){
    for(auto ch:g[node]){
      if(ch==parent)continue;
      depth[ch]=depth[node]+1;
      up[0][ch]=node;
      repl(i,1,LOG){
        up[i][ch]=up[i-1][up[i-1][ch]];
      }
      dfs(ch,node);
    }
}

int get_lca(int a,int b){
    if(depth[a]<depth[b]){
      swap(a,b);
    }
    int k=depth[a]-depth[b];
    repr(i,LOG-1){
      if((k>>i)&1){
        a=up[i][a];
      }
    }
    if(a==b){
      return a;
    }
    repr(i,LOG-1){
      if(up[i][a]!=up[i][b]){
        a=up[i][a];
        b=up[i][b];
      }
    }
    return up[0][a];

}

void solve(){
    int n,m;
    cin>>n>>m;
    g.resize(n,vector<int>());
    rep(i,n-1){
        int x,y;
        cin>>x>>y;
        x--,y--;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    dfs(0,-1);
    rep(i,m){
      int x,y;
      cin>>x>>y;
      x--,y--;
      int lca=get_lca(x,y);
      int ans=depth[x]-depth[lca]+depth[y]-depth[lca];
      cout<<ans<<endl;
    }

    
}

signed main()
{
  // freopen("cses.txt", "r", stdin);
  // freopen("out.txt", "w", stdout);
  fastIO;
  auto start = chrono::steady_clock::now();
  int t = 1;
  // cin>>t;
  while (t--)
  {
    solve();
  }
  auto end = chrono::steady_clock::now();
  auto diff = end - start;
  // cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
}
