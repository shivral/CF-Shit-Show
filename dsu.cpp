
class DSU{
    public:
        DSU(int n){
            this->n=n;
            this->parent.resize(n);
            this->sz.resize(n);
        }
        void make_set(int v){
            parent[v]=v;
            sz[v]=1;
        }

        int find_set(int v){
            if(v==parent[v]){
                return v;
            }
            parent[v]=find_set(parent[v]);
            return parent[v];
        }

        void union_set(int a,int b){
            a=find_set(a);
            b=find_set(b);
            if(a==b){
                return;
            }
            if(sz[a]<sz[b]){
                swap(a,b);
            }
            parent[b]=a;
            sz[a]+=sz[b];
        }
        


    private:
        vector<int>parent;
        vector<int>sz;
        int n;
};

