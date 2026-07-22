class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        def get_ordered(s):
            n = len(s)
            s = s + s
            i, j, k = 0, 1, 0
            while i < n and j < n and k < n:
                if s[i+k] == s[j+k]:
                    k += 1
                elif s[i+k] < s[j+k]:
                    j += k + 1
                    if i == j:
                        j += 1
                    k = 0
                else:
                    i += k + 1
                    if i == j:
                        i += 1
                    k = 0
            start = min(i, j)
            return s[start:start+n]

        group = set()
        for wd in words:
            even = []
            odd = []
            for idx, ch in enumerate(wd):
                if idx % 2 == 0:
                    even.append(ch)
                else:
                    odd.append(ch)
            ek = get_ordered(''.join(even))
            ok = get_ordered(''.join(odd))
            key = (ek, ok)
            group.add(key)
        return len(group)
                