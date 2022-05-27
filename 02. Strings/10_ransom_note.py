class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        word_hash = {}

        for char in ransomNote:
            if char in word_hash:
                word_hash[char] += 1
            else:
                word_hash[char] = 1

        # print(word_hash)

        for char in magazine:
            if char in word_hash and word_hash[char] != 0:
                word_hash[char] -= 1

        for char in word_hash:
            if word_hash[char] != 0:
                return False
            # print(char, word_hash[char])
        return True


ransomNote = "aabb"
magazine = "aab"

print(Solution().canConstruct(ransomNote, magazine))