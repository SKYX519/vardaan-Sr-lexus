class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        ans = []

        for start in range(word_len):
            left = start
            right = start
            count = 0
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in target:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right

        return ans