class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) < 1 or words is None:
            return []
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None
        rows, cols = len(board), len(board[0])
        ans = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        def dfs(r,c,parent):
            ch = board[r][c]
            if ch not in parent.children:
                return
            board[r][c] = "#"
            node = parent.children[ch]
            if node.word:
                ans.append(node.word)
                node.word = None
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr,nc,node)
            board[r][c] = ch
            if not node.children and node.word is None:
                del parent.children[ch]
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return ans