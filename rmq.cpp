class SparseTable{
    private:
        vector<vector<ll>> Table,Table1;
        vector<ll> log;
    public:
        SparseTable(vector<ll> arr){
            ll n = arr.size();
            ll k = log2(n);
            Table.resize(k+1,vector<ll>(n,0));
            Table1.resize(k+1,vector<ll>(n,0));
            log.resize(n+1);
            Table[0] = arr;
            Table1[0] = arr;
            for(ll i=1;i<=k;i++){
                for(ll j=0;j<=n-(1LL<<i);j++){
                    Table[i][j] = min(Table[i-1][j],Table[i-1][j+(1LL<<(i-1LL))]);
                    Table1[i][j] = max(Table1[i-1][j],Table1[i-1][j+(1LL<<(i-1LL))]);
                }
            }
            for(ll i=1;i<=n;i++){
                log[i] = log2(i);
            }
        }
        long long int queryMIN(ll l,ll r){
            ll k = log[r-l+1];
            return min(Table[k][l-1],Table[k][r-(1LL<<k)]);
        }
        long long int queryMAX(ll l,ll r){
            ll k = log[r-l+1];
            return max(Table1[k][l-1],Table1[k][r-(1LL<<k)]);
        }
};
