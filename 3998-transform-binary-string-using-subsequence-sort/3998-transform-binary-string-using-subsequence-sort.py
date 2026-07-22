class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n = len(s)
        ones_s = s.count('1')

        # Prefix ones in s
        prefix_s = [0] * (n + 1)
        for i in range(n):
            prefix_s[i+1] = prefix_s[i] + (s[i] == '1')

        ans = []

        for t in strs:
            fixed_ones = sum(c == '1' for c in t)
            q_positions = [i for i, c in enumerate(t) if c == '?']

            need = ones_s - fixed_ones
            if need < 0 or need > len(q_positions):
                ans.append(False)
                continue
            t_final = list(t)
            for i in range(len(q_positions) - need):
                t_final[q_positions[i]] = '0'
            for i in range(len(q_positions) - need, len(q_positions)):
                t_final[q_positions[i]] = '1'
            ok = True
            prefix_t = 0
            for i in range(n):
                if t_final[i] == '1':
                    prefix_t += 1
                if prefix_t > prefix_s[i+1]:
                    ok = False
                    break

            ans.append(ok)

        return ans