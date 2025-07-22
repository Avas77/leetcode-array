from typing import List

class Solution:
    def common_string(self, str1, str2):
        common = []
        small_len = min(len(str1), len(str2))
        for index in range(small_len):
            if str1[index] == str2[index]:
                common.append(str1[index])
            else:
                break
        return common

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        common = self.common_string(strs[0], strs[1])

        for i in range(2, len(strs)):
            common = self.common_string("".join(common), strs[i])
            if not common:
                return ""

        return "".join(common)
