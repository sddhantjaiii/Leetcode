class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int n = answers.size();
        int count = 0 ;  
        unordered_map<int , int> mp ; 
        for(int i=0 ; i<n ; i++){
            if(++mp[(answers[i]+1)]==(answers[i]+1)){
                mp[answers[i]+1]=0;
                count+=(answers[i]+1);
            }
        }
        for(auto vals: mp){
            if(vals.second>0){
                count+=(vals.first);
            }
        }
        return count ; 
    }
};