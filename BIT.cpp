#include <bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
using namespace std;
const int mxN=1e5+10;
// #define int long long
int32_t mod = 1e9 + 7;
 
#define MAX_N 100001
// auto cmp = [](auto left, auto right) { return (right.first ) < (left.first ); }; //ascending
// auto cmp2 = [](int left, int right) { return (left ) < (right); }; //descending
#define pii pair<int, int>
#include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds;
// template<class T> 
// using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;//find by order

 class FenTree{
     public:
        FenTree(int n){
            this->size=n+1;
            this->tree.resize(size);
        }
        int sum(int i){
            int res=0;
            for(++i;i>0;i-=i&-i){
                res+=tree[i];
            }
            return res;

        }
        int add(int id,int delta){
            for(++id;id<size;id+=id&(-id)){
                tree[id]+=delta;
            }
          return 0;
        }
     void clear(){
            this->tree.clear();
            this->tree.resize(this->size,0);

        }


    private:
        vector<int>tree;
        int size;

 };


struct point{
    int l;
    int r;
    int id;
};
auto cmp = [](point a, point b) { 
    if (a.l==b.l){
       return  a.r>=b.r;
    }
    return (a.l ) < (b.l ); 
    
    }; //ascending
auto cmp2 = [](point a, point b) { 
    if (a.r==b.r){
       return  a.l>=b.l;
    }
    return (a.r ) < (b.r ); 
    
    }; //ascending


void solve(){
    set<int>st;
    int n;
    cin>>n;
    int idx=0;
    vector<point>g(n);
    for(auto& i :g){
        cin>>i.l>>i.r;
        i.id=idx;
        idx++;
        st.insert(i.l);
        st.insert(i.r);
    }
    // unordered_map<int ,int> mp;
    cc_hash_table<int, int> mp;
    int base=1;
    for(auto i :st){
        mp[i]=base;
        base++;
    }
    FenTree ft(base+1);
    sort(g.begin(),g.end(),cmp);
    vector<int>vis(n);
    vector<int>vis2(n);
    for(auto i :g){
        int l=mp[i.l];
        int r=mp[i.r];
        vis[i.id]=min(ft.sum(base)-ft.sum(r-1),1);
        ft.add(r,1);
    }
    sort(g.begin(),g.end(),cmp2);
    FenTree ft2(base+1);
    for(auto i :g){
        int l=mp[i.l];
        int r=mp[i.r];
        vis2[i.id]=min(ft2.sum(base)-ft2.sum(l-1),1);
        ft2.add(l,1);
    }
    
    for(auto i :vis2){
        cout<<i<<" ";
    }
    cout<<endl;
    
    for(auto i :vis){
        cout<<i<<" ";
    }



 
}
 
 
signed main(){
    fastIO;
    int t;
    
        solve();
    
    
  
}
