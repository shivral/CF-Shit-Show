#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 1e9+7;
 
 
int main(){
    ll n;
    cin>>n;
    vector <int> values(n);
    for(int &i : values) cin>>i;
    vector <int> lis;
    for(int i = 0; i<n; i++) {
        auto it = lower_bound(lis.begin(), lis.end(), values[i]);
        if(it == lis.end()) lis.push_back(values[i]); 
        else lis[it-lis.begin()] = values[i];
    }    
    cout<<lis.size()<<endl;
    
    return 0;
}
