#include <bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
using namespace std;
// #define int long long
int32_t mod = 1e9 + 7;
#define MAX_N 100001
auto cmp = [](int left, int right) { return (right ) < (left ); }; //ascending
auto cmp2 = [](int left, int right) { return (left ) < (right); }; //descending
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds;
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
#define pii pair<int, int>

// vector<vector<int>> tree;
// vector<bool> vis;
//https://codeforces.com/gym/309368/problem/E
void solve(){
    
}


signed main(){
    fastIO;
    int n,q,temp;
    cin>>n>>q;
    vector<int>ar(n);
    pii x;
    ordered_set<pii> oset;
    for(int i=0;i<n;i++){
        cin>>ar[i];
        x={ar[i],i};
        oset.insert(x);
    }
    
    while(q--){
        int k;
        cin>>k;
        auto it=oset.find_by_order(k-1);
        cout<<it->first<<"\n";
        oset.erase(it);
    }
    return 0;
}
