class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_words = []
        for word in strs:
            encoded_words.append(str(len(word)))
            encoded_words.append('#')
            encoded_words.append(word)
        return "".join(encoded_words)

    def decode(self, s: str) -> List[str]:
        words = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            words.append(s[i:j])
            i = j

        return words