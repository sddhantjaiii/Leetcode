class Solution {
public:
    int minimumLength(string s) {
        if(s.size()<1) return 0;
        if(s.size()<2) return 1;
        if(s.size()<3) return 2;
        int hash[26]={0};
        for(int i=0;i<s.size();i++){
            hash[s[i]-'a']++;
        }
        int x=0;
        for(int i=0;i<26;i++){
            while(hash[i]>=3){
                hash[i]-=2;
            }
            x+=hash[i];
        }
        return x;
    }
};