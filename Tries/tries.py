class TrieNode:
    def __init__(self, val=None, child={}, is_word=False):
        self.val = val
        self.children = child
        self.is_word = is_word

    def add_child(self,cval):
        self.children[cval] = self.children.get(cval,TrieNode(cval,{}))
        return self.children[cval]
    
lw = ['many','man','my','lie','line']

trie = TrieNode()
for w in lw:
    cr = trie
    for c in w:
        cr = cr.add_child(c)
    cr.is_word=True
    

def dfs(root):
    print(root.val)
    for c in root.children:
        cr = root.children[c]
        #print(cr.val)
        dfs(cr)

        

dfs(trie)
#print(trie.children['l'].children['i'].children['n'].children['e'].children)