class Solution {
public:
    int n;
    int len;
    int dp[102][102];
    int solve(int ind, int prev, vector<string> &strs)
    {
        if(ind==n) return 0;
        if(dp[ind][prev+1]!=-1) return dp[ind][prev+1];
        if(prev==-1) // first ind not chosen yet -> can either choose current ind as first or move forward without choosing
        {
            return dp[ind][prev+1]=min(solve(ind+1,ind,strs),1+solve(ind+1,prev,strs));
        }

        bool flg = true; //considering true
        for(auto x:strs)
        {
            if(x[prev]>x[ind]) {flg=false; break;}
        }

        if(flg) //condition is true -> we can delete ind or not delete
        {
            return dp[ind][prev+1]=min(solve(ind+1,ind,strs), 1+solve(ind+1,prev,strs));
            
        }

        //condition is false -> WE HAVE TO DELETE IND

        return dp[ind][prev+1]=1+solve(ind+1,prev,strs);

    }
    int minDeletionSize(vector<string>& strs) {
        n = strs[0].size();
        memset(dp,-1,sizeof(dp));
        return solve(0,-1,strs);
    }
};