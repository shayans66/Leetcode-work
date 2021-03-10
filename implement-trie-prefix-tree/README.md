<h2>208. Implement Trie (Prefix Tree)</h2><h3>Medium</h3><hr><div><p>Trie (we pronounce "try") or prefix tree is a tree data structure used to retrieve a key in a strings dataset. There are various applications of this very efficient data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> initializes the trie object.</li>
	<li><code>void insert(String word)</code> inserts the string <code>word</code> to the trie.</li>
	<li><code>boolean search(String word)</code> returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>
</div>