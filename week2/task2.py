"""
https://leetcode.com/problems/text-justification/description/

"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        n = len(words)
        result = []
        i = 0
        while i < n:
            cur_string = ""
            if i == n - 1 or maxWidth - len(words[i]) <= len(words[i + 1]):
                cur_string += words[i]
                cur_string += " " * (maxWidth - len(words[i]))
                i += 1
            else:
                cur_len = 0
                j = i
                word_count = 0
                while i < n and cur_len + len(words[i]) + word_count <= maxWidth:
                    word_count += 1
                    cur_len += len(words[i])
                    i += 1
                fill = (
                    (maxWidth - cur_len - word_count + 1) // (word_count - 1)
                    if word_count > 1
                    else 0
                )
                dop_fill = (
                    (maxWidth - cur_len - word_count + 1) % (word_count - 1)
                    if word_count > 1
                    else 0
                )
                if i == n:
                    for k in range(j, n):
                        cur_string += words[k]
                        if k != n - 1:
                            cur_string += " "
                    cur_string += " " * (maxWidth - cur_len - word_count + 1)
                else:
                    for k in range(j, i - 1):
                        cur_string += words[k]
                        cur_string += " " * (fill + 1)
                        if dop_fill:
                            cur_string += " "
                            dop_fill -= 1
                    cur_string += words[i - 1]

            result.append(cur_string)

        return result
