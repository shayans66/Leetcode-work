
class Solution {
public:
    bool isValid(string s) {
        
        stack<string> st;
        unordered_map<string, string> map;
        map[")"] = "(";
        map["]"] = "[";
        map["}"] = "{";
        
        for(int i=0; i < s.size(); i++){
            if(map.find(string(1,s[i])) != map.end() ){
                string topelem = !st.empty() ? st.top() : "#";
                if(!st.empty())
                    st.pop();

                if( map[string(1, s[i])] != string(1, topelem[0]) )
                    return false;
            }
            else
               st.push(string(1, s[i]));
        }
        return st.empty();
    }
};