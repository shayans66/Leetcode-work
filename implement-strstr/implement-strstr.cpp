class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle == "")
            return 0;
        if(needle.length() > haystack.size())
            return -1;
        for(int i=0; i < haystack.length() - needle.length() + 1; i++){
            for(int j=0; j < needle.length(); j++){
                if(haystack[i+j] != needle[j])
                    break;
                else if(j == needle.length()-1)
                    return i;
            }
        }
        return -1;
    }
};