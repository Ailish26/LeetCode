class Solution:
    def toLowerCase(self, s: str) -> str:
        finalString = ""
        for i in range(len(s)):
            if s[i] == 'A':
                finalString += 'a'
            elif s[i] == 'B':
                finalString += 'b'
            elif s[i] == 'C':
                finalString += 'c'
            elif s[i] == 'D':
                finalString += 'd'
            elif s[i] == 'E':
                finalString += 'e'
            elif s[i] == 'F':
                finalString += 'f'
            elif s[i] == 'G':
                finalString += 'g'
            elif s[i] == 'H':
                finalString += 'h'
            elif s[i] == 'I':
                finalString += 'i'
            elif s[i] == 'J':
                finalString += 'j'
            elif s[i] == 'K':
                finalString += 'k'
            elif s[i] == 'L':
                finalString += 'l'
            elif s[i] == 'M':
                finalString += 'm'
            elif s[i] == 'N':
                finalString += 'n'
            elif s[i] == 'Ñ':
                finalString += 'ñ'
            elif s[i] == 'O':
                finalString += 'o'
            elif s[i] == 'P':
                finalString += 'p'
            elif s[i] == 'Q':
                finalString += 'q'
            elif s[i] == 'R':
                finalString += 'r'
            elif s[i] == 'S':
                finalString += 's'
            elif s[i] == 'T':
                finalString += 't'
            elif s[i] == 'U':
                finalString += 'u'
            elif s[i] == 'V':
                finalString += 'v'
            elif s[i] == 'W':
                finalString += 'w'
            elif s[i] == 'Y':
                finalString += 'y'
            elif s[i] == 'X':
                finalString += 'x'
            elif s[i] == 'Z':
                finalString += 'z'
            else:
                finalString += s[i]
        return finalString