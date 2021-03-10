class Trie {
public:
    // get index of m_children in TrieNode given a char
    int getInd(char ch){
        if( ch == '\'' )
            return 26;
        int ind = tolower(ch) - 'a';
        if(ind<0 || ind >25)
            return -1;
        return ind;
    }
    
    /** Initialize your data structure here. */
    struct TrieNode{
        TrieNode(){
            for(int i=0; i < 27; i++)
                m_children[i] = nullptr;
            m_isEndOfWord = false;
        }
        

        
        bool m_isEndOfWord;
        struct TrieNode * m_children[ 27 ];
    };
    
    // root node of trie
    TrieNode *m_root;
    
    
    TrieNode* getNode(){
        TrieNode* p = new TrieNode;
        return p;
    }
    
    Trie() {
        m_root = getNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        
        TrieNode *crawler = m_root;
        
        for(int i = 0; i < word.size(); i++){
            // get index for m_children for current char
            int ind = getInd(word[i]);
            // if ind out of bound, continue
            if( ind < 0 || ind >= 27 )
                continue;
            // if cur char isn't defined, define it
            if( ! crawler->m_children[ind] )
                crawler->m_children[ind] = getNode();
            // move to next char
            crawler = crawler->m_children[ind];
        }
        // inserted all of the chars, indicate end of word
        crawler->m_isEndOfWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *crawler = m_root;
        
        if( !m_root )
            return false;
        
        for(int i = 0; i < word.size(); i++){
            // get index for m_children for current char
            int ind = getInd(word[i]);
            // if cur char isn't defined, fail
            if( ! crawler->m_children[ind] )
                return false;
            // move to next char
            crawler = crawler->m_children[ind];
        }
        // if crawler is at end of word, ret true
        return crawler != nullptr && crawler->m_isEndOfWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string word) {
        TrieNode *crawler = m_root;
        
        if( !m_root )
            return false;
        
        for(int i = 0; i < word.size(); i++){
            // get index for m_children for current char
            int ind = getInd(word[i]);
            // if cur char isn't defined, fail
            if( ! crawler->m_children[ind] )
                return false;
            // move to next char
            crawler = crawler->m_children[ind];
        }
        // if crawler is at end of word, ret true
        return crawler != nullptr;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */