#include <bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
using namespace std;
#define int long long
#define pii pair<int, int>
int32_t mod = 1e9 + 7;
#define MAX_N 100001
auto cmp = [](auto left, auto right) { return (right.second ) < (left.second ); }; //descending
auto cmp2 = [](int left, int right) { return (left ) < (right); }; //ascending
// vector<vector<int>> tree;
// vector<bool> vis;

 
void print_map(const map<int, int>& m)
{
    for (auto it : m) {
        std::cout << it.first << " = " << it.second << "; ";
    }
    std::cout << "\n";
}
void solve(){
    std::set<pair<int,int>,decltype(cmp)> a(cmp);
  a.insert({1,100});
  a.insert({100,2});
  a.insert({300,1000});
  for(auto i: a) std::cout << i.first << ' '<<i.second<<"\n";
  std::cout << '\n';
    std::map<int, int> m;
    m[1] = 1000;
    m[2] = 20;
    m[3] = 300;
    m[4] = 40;
    m[5] = 50;
    m[6] = 60;
    print_map(m);
    
  
 
 
}


signed main(){
    
    fastIO;
   
    solve();
    return 0;
}
