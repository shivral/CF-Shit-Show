class SparseTable{
    private:
        vector<vector<int>> Table,Table1;
        vector<int> log;
    public:
        SparseTable(vector<int> arr){
            int n = arr.size();
            int k = log2(n);
            Table.resize(k+1,vector<int>(n,0));
            Table1.resize(k+1,vector<int>(n,0));
            log.resize(n+1);
            Table[0] = arr;
            Table1[0] = arr;
            for(int i=1;i<=k;i++){
                for(int j=0;j<=n-(1LL<<i);j++){
                    Table[i][j] = min(Table[i-1][j],Table[i-1][j+(1LL<<(i-1LL))]);
                    Table1[i][j] = max(Table1[i-1][j],Table1[i-1][j+(1LL<<(i-1LL))]);
                }
            }
            for(int i=1;i<=n;i++){
                log[i] = log2(i);
            }
        }
        int queryMIN(int l,int r){
            int k = log[r-l+1];
            return min(Table[k][l-1],Table[k][r-(1LL<<k)]);
        }
        int queryMAX(int l,int r){
            int k = log[r-l+1];
            return max(Table1[k][l-1],Table1[k][r-(1LL<<k)]);
        }
};
