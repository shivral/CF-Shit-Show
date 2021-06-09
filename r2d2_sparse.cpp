#include <cstdio>
#include <cmath>
using namespace std;
#define N 100005
#define M 31
#define max(a, b)  (a) > (b) ? (a) : (b)
int dp[N][M][5], detail[N][5], res[5], n, m, k;

inline int query(int a, int b, int type){
	int t = log((double)(b - a + 1))/log(2.0);
	return max(dp[a][t][type], dp[b - (1 << t) + 1][t][type]);
}

bool check(int len){
	int bound = n - len, need[5];
    for(int i = 0; i <= bound; ++i){
    	int j = i + len - 1, total = 0;
    	for(int s = 0; s < m; ++s){
    		need[s] = query(i, j, s);
    		total += need[s];
    	}
    	if(total <= k){
    		for(int s = 0; s < m; ++s)
    			res[s] = need[s];
    		return true;
    	}
    }
    return false;
}

int main(){
	scanf("%d %d %d", &n, &m, &k);
	for(int i = 0; i < n; ++i){
		for(int j = 0; j < m; ++j)
			scanf("%d", &detail[i][j]);
	}
	for(int t = 0; t < m; ++t){
	    for(int i = 0; i < n; ++i)
            dp[i][0][t] = detail[i][t];
		for(int j = 1; j < M; ++j){
			for(int i = 0; i < n; ++i){
				int tmp = i + (1 << (j - 1));
				if(tmp >= n)
					break;
				dp[i][j][t] = max(dp[i][j - 1][t], dp[tmp][j - 1][t]);
			}
		}
	}
	int l = 1, r = n;
	while(l < r - 1){
        int mid = l + ((r - l) >> 1);
        if(check(mid))
        	l = mid;
        else
        	r = mid - 1;
	}
	check(r);
	for(int i = 0; i < m; ++i)
		printf("%d ", res[i]);
	printf("\n");
	return 0;
}
