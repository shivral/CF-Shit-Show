#include <bits/stdc++.h>
using namespace std;
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
const int mxN=1e5+10;
#define int long long
int32_t mod = 1e9 + 7;
#define MAX_N 100001
auto cmp = [](auto left, auto right) { return (right.first ) < (left.first ); }; //ascending
auto cmp2 = [](auto left, auto right) { return (left.first ) < (right.first); }; //descending
#define pii pair<int, int>
#define rep(i, n) for(int i = 0; i < n; ++i)
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp> 
// using namespace __gnu_pbds;
// template<class T> 
// using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;//find by order
void Print(int32_t x) {cout << x << " ";} void Print(char x) {cout << x << " ";} void Print(const char *x) {cout << x << " ";} void Print(double x) {cout << x << " ";} void Print(int x) {cout << x << " ";} void print() {cout << endl;}
void Print(bool x) {cout << (x ? "YES" : "NO");} void Print(const string &x) {cout << x << " ";}  template<typename T, typename V> void Print(const pair<T, V> x) {cout << x.first << " " << x.second << endl;}
template<typename T> void Print(const T &x) {for (auto &i : x) Print(i);} template <typename T, typename... V> void print(T t, V... v) { Print(t); print(v...);}


long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}

void solve(){
    int n,m;
    cin>>n>>m;
    vector<vector<int>>g(n);
    vector<vector<int>>b(n);
    vector<int>ind(n);
    
    rep(i,m){
        int x,y;
        cin>>x>>y;
        x--,y--;
        g[x].push_back(y);
        b[y].push_back(x);
        ind[y]++;
    }

    deque<int>q;
    for(int i=0;i<n;i++){
        if(ind[i]==0)
            q.push_back(i); //kahns algorithm
    }
    vector<int>d(n);
    d[0]=1;
    while (q.size())
    {
        int t=q.front();
        q.pop_front();
        for(auto i:g[t]){
            ind[i]--;
            if(ind[i]==0)
                q.push_back(i);
        }
        for(auto i:b[t]){
            d[t]=(d[t]+d[i])%(mod);
        }
    }
    cout<<d[n-1]<<endl;
    return;
    
	} 

 
signed main(){
//    freopen("test_input(1).txt", "r", stdin);
//   freopen("out.txt", "w", stdout);
  fastIO;
  auto start = chrono::steady_clock::now();
  int t=1;
  // cin>>t;
  while(t--){
  solve();
  }
  auto end = chrono::steady_clock::now();
  auto diff = end - start;
//   cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;

  
}
