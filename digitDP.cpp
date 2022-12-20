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

//dp[nonzero][smaller][md][ind]
int dp[2][2][100][10000],m,n,lead;
string a;
string num;
int rec(int nonzero,int smaller,int md,int ind){
  if(ind==(int)num.size() ){
    return (!nonzero or md)?0:1;
  }
  if(dp[nonzero][smaller][md][ind]!=-1){

    // cout<<"bache "<<dp[nonzero][smaller][md][ind]<<endl;
    return dp[nonzero][smaller][md][ind];
    }
  int range=(smaller)?9:num[ind]-'0';
  int ans=0;
  // cout<<"range "<<range<<endl;
  for(int i=0;i<=range;i++){
    int n_nonzero=(nonzero|(i>0));
    int n_smaller=(smaller|(i<range));
    int n_md=(md+(i%m))%m;
    ans+=(rec(n_nonzero,n_smaller,n_md,ind+1));
    ans%=mod;
  }
 
 
  dp[nonzero][smaller][md][ind]=ans;
  // cout<<"ans here "<<ans<<endl;
  return ans;
}

void solve(){
cin>>num;
cin>>m;
// cout<<" lol"<<n<<m<<a<<b<<endl;
memset(dp,-1,sizeof(dp));
// int ans1=0;
int ans1=rec(0,0,0,0);
cout<<ans1<<endl;

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
